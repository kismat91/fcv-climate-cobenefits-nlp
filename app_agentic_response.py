import streamlit as st
import pandas as pd
import numpy as np
import tiktoken
from openai import OpenAI
import os
import altair as alt
import json
import time
from io import BytesIO
from datetime import datetime
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from pymongo import MongoClient
from prompts import ALL_PROMPTS
import uuid
import hashlib

from extract_scores import extract_score_probabilities_and_scores

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = None
if openai_api_key:
    client = OpenAI(api_key=openai_api_key)
else:
    st.warning("OpenAI API key not found. Please set OPENAI_API_KEY in your environment.")

# MongoDB connection with TLS settings (using invalid certificates for testing)
mongo_client = MongoClient(
    'mongodb+srv://Mongo:SecureMongo@cluster0.poitw.mongodb.net/',
    tls=True,
    tlsAllowInvalidCertificates=True
)
db = mongo_client['projects_db']  # Replace with your database name
collection = db['wb_projects']
# Collection to store mapping: document hash to vector store ID.
mappings_collection = db['vector_store_mappings']

# Streamlit page config
st.set_page_config(
    page_title="World Bank AI Analyzer 🌍",
    page_icon="🌍",
    layout="wide"
)


###########################################
# 1. CUSTOM CSS
###########################################
def add_custom_css():
    st.markdown("""
        <style>
        /* Hide default Streamlit elements */
        #MainMenu, header, footer {visibility: hidden;}

        body {
            background-color: #F9FAFC;
        }

        .block-container {
            padding: 2rem;
            background-color: #FFFFFF;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0,0,0,0.05);
        }

        h1, h2, h3, h4, h5, h6 {
            color: #212121;
            font-family: "Raleway", sans-serif;
        }
        p, div, label, span {
            color: #424242;
            font-family: "Open Sans", sans-serif;
        }

        .streamlit-expanderHeader {
            font-weight: 700;
            color: #333333;
        }

        /* Simple chat message styles */
        .chat-user {
            background-color: #DCF8C6;
            padding: 8px 12px;
            border-radius: 12px;
            margin-bottom: 8px;
            text-align: right;
            max-width: 80%;
        }
        .chat-assistant {
            background-color: #ECECEC;
            padding: 8px 12px;
            border-radius: 12px;
            margin-bottom: 8px;
            text-align: left;
            max-width: 80%;
        }

        .stTabs [data-baseweb="tab"] {
            font-size: 1rem;
            padding: 10px;
            color: #777777;
        }
        .stTabs [data-baseweb="tab"].stTabActive {
            font-weight: 700;
            color: #0B5394;
            border-bottom: 3px solid #0B5394 !important;
        }
        </style>
    """, unsafe_allow_html=True)


###########################################
# 2. GLOBAL PRICING & UTILITIES
###########################################

PRICING = {
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-4o-realtime-preview": {"input": 5.00, "output": 20.00},
    "gpt-4o-mini-realtime-preview": {"input": 0.60, "output": 2.40},
    "o1": {"input": 15.00, "output": 60.00},
    "o3-mini": {"input": 1.10, "output": 4.40},
    "o1-mini": {"input": 1.10, "output": 4.40}
}


def count_tokens(text, model="gpt-4o-mini"):
    try:
        enc = tiktoken.encoding_for_model(model)
        return len(enc.encode(text))
    except KeyError:
        return len(text.split())


def calculate_cost(input_tokens, output_tokens, model):
    if model in PRICING:
        input_cost_per_million = PRICING[model]["input"]
        output_cost_per_million = PRICING[model]["output"]
        input_cost = (input_tokens / 1_000_000) * input_cost_per_million
        output_cost = (output_tokens / 1_000_000) * output_cost_per_million
        total_cost = input_cost + output_cost
        return round(input_cost, 6), round(output_cost, 6), round(total_cost, 6)
    return 0.0, 0.0, 0.0


def parse_fcv_scores(response_text):
    lines = response_text.splitlines()
    scored_lines = []
    for line in lines:
        if "Score:" in line:
            score_str = line.split("Score:")[-1].strip()
            try:
                score_val = int(score_str)
                if score_val == 3:
                    color_emoji = "✅ (Green)"
                elif score_val == 2:
                    color_emoji = "🟡 (Yellow)"
                elif score_val == 1:
                    color_emoji = "🟠 (Orange)"
                else:
                    color_emoji = "🔴 (Red)"
                scored_lines.append(f"{line}  {color_emoji}")
            except ValueError:
                scored_lines.append(line)
        else:
            scored_lines.append(line)
    return "\n".join(scored_lines)


def load_dataset():
    url = "hf://datasets/lukesjordan/worldbank-project-documents/wb_project_documents.jsonl.gz"
    df = pd.read_json(url, lines=True, compression="gzip")
    return df


def get_document_text(df, project_id):
    project_data = df[df["project_id"] == project_id]
    if not project_data.empty:
        return project_data["document_text"].iloc[0]
    else:
        return None


def parse_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension == "pdf":
            reader = PdfReader(uploaded_file)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text
        else:
            return uploaded_file.read().decode("utf-8", errors="replace")
    return None


###########################################
# 3. INDEXING & QUERY FUNCTIONS
###########################################

class NamedBytesIO(BytesIO):
    def __init__(self, initial_bytes, name):
        super().__init__(initial_bytes)
        self.name = name


def get_document_hash(document_text):
    return hashlib.md5(document_text.encode("utf-8")).hexdigest()


def get_vector_store_mapping(doc_hash):
    mapping_doc = mappings_collection.find_one({"doc_hash": doc_hash})
    if mapping_doc:
        return mapping_doc.get("vector_store_id")
    return None


def set_vector_store_mapping(doc_hash, vector_store_id):
    mappings_collection.update_one(
        {"doc_hash": doc_hash},
        {"$set": {"vector_store_id": vector_store_id}},
        upsert=True
    )


def create_vector_store():
    try:
        response = client.vector_stores.create(name="Document Index")
        st.write("Created vector store:", response)
        vector_store_id = response.id
        if not vector_store_id:
            st.error("Failed to retrieve vector store id from response.")
        return vector_store_id
    except Exception as e:
        st.error(f"Error creating vector store: {e}")
        return None


def upload_document_as_file(document_text):
    try:
        file_bytes = NamedBytesIO(document_text.encode("utf-8"), name="document.txt")
        response = client.files.create(file=file_bytes, purpose="assistants")
        st.write("Uploaded file:", response)
        file_id = response.id
        return file_id
    except Exception as e:
        st.error(f"Error uploading file: {e}")
        return None


def attach_file_to_vector_store(vector_store_id, file_id):
    try:
        vector_store_file = client.vector_stores.files.create(
            vector_store_id=vector_store_id,
            file_id=file_id
        )
        st.write("Attached file to vector store:", vector_store_file)
        return vector_store_file
    except Exception as e:
        st.error(f"Error attaching file to vector store: {e}")
        return None


def index_document(document_text):
    doc_hash = get_document_hash(document_text)
    existing_vs_id = get_vector_store_mapping(doc_hash)
    if existing_vs_id:
        st.info("Reusing existing vector store for this document.")
        return existing_vs_id

    new_vector_store_id = create_vector_store()
    if new_vector_store_id is None:
        st.error("Failed to create vector store.")
        return None

    file_id = upload_document_as_file(document_text)
    if file_id is None:
        st.error("Failed to upload document as a file.")
        return None

    attach_resp = attach_file_to_vector_store(new_vector_store_id, file_id)
    # Update mapping for future reuse.
    set_vector_store_mapping(doc_hash, new_vector_store_id)

    response = client.responses.create(
        model=st.session_state["selected_model"],
        input=document_text,
        tools=[{"type": "file_search", "vector_store_ids": [new_vector_store_id]}]
    )
    st.write("Indexing response:", response)
    return new_vector_store_id


def query_document(question, vector_store_id, selected_model):
    COST_PER_1K_INPUT = 0.005
    COST_PER_1K_OUTPUT = 0.015
    try:
        response = client.responses.create(
            model=selected_model,
            input=question,
            tools=[{
                "type": "file_search",
                "vector_store_ids": [vector_store_id],
                "max_num_results": 5
            }]
        )
        try:
            answer = response.output[1].content[0].text
        except AttributeError:
            if hasattr(response.output[1], 'results') and response.output[1].results:
                answer = " ".join([res.get("content", "") for res in response.output[1].results])
            else:
                answer = "No relevant results found."
        usage = response.usage
        input_tokens = usage.input_tokens
        output_tokens = usage.output_tokens
        input_cost = (input_tokens / 1000) * COST_PER_1K_INPUT
        output_cost = (output_tokens / 1000) * COST_PER_1K_OUTPUT
        total_cost = input_cost + output_cost
        answer += (
            "\n\n---\n"
            "🧮 **Usage Summary**\n"
            f"- Input tokens: {input_tokens}\n"
            f"- Output tokens: {output_tokens}\n"
            f"- 💰 Estimated cost: ${total_cost:.5f}"
        )
    except Exception as e:
        answer = f"❌ Error: {e}"
        input_tokens = output_tokens = input_cost = output_cost = total_cost = 0
    return answer, input_tokens, output_tokens, input_cost, output_cost, total_cost


###########################################
# 4. USAGE TRACKING & EXPORT FUNCTIONS
###########################################
def add_usage_history(input_tokens, output_tokens, total_cost):
    if "usage_history" not in st.session_state:
        st.session_state["usage_history"] = []
    st.session_state["usage_history"].append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "cost": total_cost
    })


def get_usage_history_df():
    if "usage_history" not in st.session_state:
        st.session_state["usage_history"] = []
    return pd.DataFrame(st.session_state["usage_history"])


def export_report_as_pdf(response_text):
    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer)
    styles = getSampleStyleSheet()
    lines = response_text.split("\n")
    story = [Paragraph(line, styles["Normal"]) for line in lines]
    doc.build(story)
    return pdf_buffer.getvalue()


def export_report_as_csv(response_text):
    lines = response_text.split("\n")
    df = pd.DataFrame({"Analysis": lines})
    return df.to_csv(index=False).encode("utf-8")


def export_report_as_json(response_text):
    lines = response_text.split("\n")
    return json.dumps({"analysis": lines}, indent=2).encode("utf-8")

# Display Extracted Results
def display_extracted_results(llm_output):
    """
    Display results extracted from the extract_score_probabilities_and_scores function.
    """

    extracted_results, total_score = extract_score_probabilities_and_scores(llm_output)

    st.subheader("Extracted Results")
    st.write(f"**Total FCV Sensitivity Score:** {total_score}")

    for characteristic, questions in extracted_results.items():
        with st.expander(f"Characteristic: {characteristic}", expanded=False):
            for question_data in questions:
                st.markdown(f"**Question:** {question_data['question']}")
                st.markdown(f"**Score:** {question_data['score']}")
                st.markdown(f"**Probabilities:** {question_data['probabilities']}")
                st.markdown("---")

###########################################
# 5. MONGODB HELPERS
###########################################
def get_all_project_ids_from_db():
    docs = collection.find({}, {"project_id": 1})
    return [d["project_id"] for d in docs if "project_id" in d]


def get_document_text_from_db(project_id):
    doc = collection.find_one({"project_id": project_id})
    if doc:
        return doc.get("pad_doc", "")
    return None


###########################################
# 6. MAIN APP
###########################################
def main():
    add_custom_css()

    if "selected_model" not in st.session_state:
        st.session_state["selected_model"] = "gpt-4o-mini"
    if "temperature" not in st.session_state:
        st.session_state["temperature"] = 0.8
    if "max_tokens" not in st.session_state:
        st.session_state["max_tokens"] = 2000
    if "selected_prompt" not in st.session_state:
        st.session_state["selected_prompt"] = "Prompt 4 (Probabilities)"

    # --- In your MAIN APP, after protocol update, in the sidebar ---

    # Sidebar: Prompt Selector and Protocol Editor
    st.sidebar.title("World Bank AI Analyzer 🌍")
    st.sidebar.markdown("---")

    prompt_list = list(ALL_PROMPTS.keys())
    default_index = prompt_list.index("Prompt 4 (Probabilities)")
    selected_prompt = st.sidebar.selectbox("Select a Prompt:", prompt_list, index=default_index)
    st.session_state["selected_prompt"] = selected_prompt
    st.session_state["protocol"] = ALL_PROMPTS[selected_prompt]

    st.sidebar.subheader("Current Protocol")
    new_protocol = st.sidebar.text_area("Edit or enter a new protocol:", st.session_state["protocol"], height=200)
    if st.sidebar.button("Update Protocol"):
        st.session_state["protocol"] = new_protocol
        st.sidebar.success("Protocol updated successfully!")

    # Store a default report query the first time a document is indexed if not already set.
    if "default_report_query" not in st.session_state and "indexed_document_text" in st.session_state:
        st.session_state["default_report_query"] = st.session_state["protocol"]
    if "vector_store_id" in st.session_state and st.session_state["vector_store_id"]:
        # Button always visible to generate a report
        # Sidebar Report Generation Section
        st.sidebar.subheader("Generate Report")
        if "vector_store_id" in st.session_state and st.session_state["vector_store_id"]:
            if st.sidebar.button("Generate Report"):
                with st.spinner("Generating report... Please wait..."):
                    # Use chat history if available, otherwise fallback to the stored default query.
                    if "chat_history" in st.session_state and st.session_state["chat_history"]:
                        report_text = "\n".join(
                            [f"{msg['role'].capitalize()}: {msg['text']}" for msg in st.session_state["chat_history"]])
                    else:
                        default_query = st.session_state.get("default_report_query", st.session_state["protocol"])
                        report_text, _, _, _, _, _ = query_document(default_query, st.session_state["vector_store_id"],
                                                                    st.session_state["selected_model"])
                    # Simulate a brief delay for UX purposes.
                    import time
                    time.sleep(1)
                with st.sidebar.expander("Report Preview", expanded=True):
                    st.markdown("### Report")
                    st.text_area("Report Content", report_text, height=200, disabled=True)
                    display_extracted_results(report_text)
                st.sidebar.download_button("Download Report (PDF)", data=export_report_as_pdf(report_text),
                                           file_name="report.pdf", mime="application/pdf")
        else:
            st.sidebar.info("Select and index a document to generate a report.")

    tabs = st.tabs(["Home 🏠", "Analyze Document 📑", "Settings ⚙️", "About ℹ️"])

    with tabs[0]:
        st.title("Welcome to the World Bank AI Analyzer 🌍")
        st.markdown("""
        This application allows you to analyze World Bank project documents using 
        OpenAI's GPT models for **Fragility, Conflict, and Violence (FCV)** sensitivity.

        **Key Features**:
        - Multiple data source options (Hugging Face, MongoDB, or your own file)
        - Retrieval-augmented Q&A with document indexing
        - Cost & token usage tracking
        - Exportable AI-generated reports (PDF, CSV, JSON)

        Use the tabs above to navigate through the app!
        """)

    with tabs[1]:
        st.header("Analyze Document 📑")
        st.write("Choose your data source, then load and analyze a document.")
        data_source = st.radio("Select Data Source:", ["Hugging Face Dataset", "MongoDB Dataset", "Upload Your File"])
        document_text = None

        if data_source == "Hugging Face Dataset":
            if "hf_df" not in st.session_state:
                st.session_state["hf_df"] = None
            if st.button("Load Hugging Face Data"):
                with st.spinner("Loading dataset from Hugging Face..."):
                    st.session_state["hf_df"] = load_dataset()
                st.success("Hugging Face dataset loaded.")
            if st.session_state["hf_df"] is not None:
                project_ids = st.session_state["hf_df"]["project_id"].unique().tolist()
                selected_project_id = st.selectbox("Select or Search Project ID:", project_ids)
                if selected_project_id:
                    document_text = get_document_text(st.session_state["hf_df"], selected_project_id)
                    if not document_text:
                        st.error("No document found for the selected Project ID.")

        elif data_source == "MongoDB Dataset":
            if "mongo_ids" not in st.session_state:
                st.session_state["mongo_ids"] = None
            if st.button("Load Project IDs from MongoDB"):
                with st.spinner("Fetching project IDs from MongoDB..."):
                    st.session_state["mongo_ids"] = get_all_project_ids_from_db()
                st.success("MongoDB project IDs loaded.")
            if st.session_state["mongo_ids"]:
                selected_mongo_project_id = st.selectbox("Select or Search Project ID from MongoDB:",
                                                         st.session_state["mongo_ids"])
                if selected_mongo_project_id:
                    document_text = get_document_text_from_db(selected_mongo_project_id)
                    if not document_text:
                        st.error("No document found for this Project ID in MongoDB.")
            else:
                st.info("Click the button above to load project IDs from MongoDB.")

        else:
            uploaded_file = st.file_uploader("Upload PDF or Text File", type=["pdf", "txt"])
            if uploaded_file:
                document_text = parse_uploaded_file(uploaded_file)
                if not document_text:
                    st.error("Could not parse the uploaded file.")

        st.markdown("---")
        if document_text:
            st.subheader("Document Preview")
            preview_snippet = document_text[:800] + ("..." if len(document_text) > 800 else "")
            st.write(preview_snippet)
            with st.expander("Show Full Document"):
                st.text_area("Full Document", document_text, height=400, disabled=True)
            st.session_state["document_text"] = document_text

            if ("indexed_document_text" not in st.session_state or st.session_state[
                "indexed_document_text"] != document_text):
                with st.spinner("Indexing document..."):
                    vector_store_id = index_document(document_text)
                    if vector_store_id:
                        st.session_state["vector_store_id"] = vector_store_id
                        st.session_state["indexed_document_text"] = document_text
                        st.success("Document indexed successfully!")
                    else:
                        st.error("Document indexing failed.")
            else:
                vector_store_id = st.session_state.get("vector_store_id", None)

            if vector_store_id:
                st.info("Document is ready for Q&A. Ask your question below:")
                if "chat_history" not in st.session_state:
                    st.session_state["chat_history"] = []
                user_question = st.chat_input("Enter your question here...")
                if user_question:
                    st.session_state.chat_history.append({"role": "user", "text": user_question})
                    with st.spinner("🤖 AI is thinking..."):
                        answer, in_tokens, out_tokens, in_cost, out_cost, tot_cost = query_document(
                            user_question, vector_store_id, st.session_state["selected_model"]
                        )
                    st.session_state.chat_history.append({"role": "assistant", "text": answer})
                    add_usage_history(in_tokens, out_tokens, tot_cost)
                chat_container = st.container()
                with chat_container:
                    for msg in st.session_state.chat_history:
                        if msg["role"] == "user":
                            st.markdown(f'<div class="chat-user"><strong>You:</strong> {msg["text"]}</div>',
                                        unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="chat-assistant"><strong>Assistant:</strong> {msg["text"]}</div>',
                                        unsafe_allow_html=True)

    with tabs[2]:
        st.header("Settings ⚙️")
        model_options = list(PRICING.keys())
        st.session_state["selected_model"] = st.selectbox("🤖 Select OpenAI Model:", model_options,
                                                          index=model_options.index(
                                                              st.session_state.get("selected_model", "gpt-4o-mini")))
        st.session_state["temperature"] = st.slider("Temperature (creativity)", 0.0, 1.0,
                                                    st.session_state["temperature"], 0.1)
        st.session_state["max_tokens"] = st.number_input("Max Tokens for Response", min_value=100, max_value=4000,
                                                         step=100, value=st.session_state["max_tokens"])
        st.subheader("Model Pricing (per 1M tokens)")
        price_df = pd.DataFrame(PRICING).T.reset_index().rename(
            columns={"index": "Model", "input": "Input ($)", "output": "Output ($)"})
        st.dataframe(price_df.style.format({"Input ($)": "{:.2f}", "Output ($)": "{:.2f}"}))
        st.subheader("Cost History & Visualization")
        usage_df = get_usage_history_df()
        if not usage_df.empty:
            st.write("Below is the usage history of your analysis sessions.")
            st.dataframe(usage_df)
            c = alt.Chart(usage_df).mark_line(point=True).encode(x="timestamp:T", y="cost:Q",
                                                                 tooltip=["timestamp", "cost"]).properties(
                title="Cost Over Time")
            st.altair_chart(c, use_container_width=True)
            c2 = alt.Chart(usage_df).mark_bar().encode(x="timestamp:T", y="total_tokens:Q",
                                                       tooltip=["timestamp", "total_tokens"]).properties(
                title="Total Tokens Over Time")
            st.altair_chart(c2, use_container_width=True)
        else:
            st.info("No usage history yet.")

    with tabs[3]:
        st.header("About ℹ️")
        st.markdown("""
        **World Bank AI Analyzer** is a Streamlit application showcasing how to integrate 
        OpenAI's GPT models for document analysis, specifically focusing on FCV (Fragility, 
        Conflict, and Violence) sensitivity.

        **Key Technologies**:
        - [Streamlit](https://streamlit.io/)
        - [OpenAI Python Client](https://pypi.org/project/openai/) for GPT Models
        - [tiktoken](https://github.com/openai/tiktoken) for token counting
        - [Altair](https://altair-viz.github.io/) for data visualization
        - [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF parsing
        - [ReportLab](https://pypi.org/project/reportlab/) for PDF report generation
        - [MongoDB](https://www.mongodb.com/) for storing and retrieving documents

        **Contact**:
        - Email: example@example.com
        - GitHub: [YourRepo](https://github.com/YourRepo)
        """)


if __name__ == "__main__":
    main()
