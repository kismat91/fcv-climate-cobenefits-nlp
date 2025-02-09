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

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = None
if openai_api_key:
    client = OpenAI(api_key=openai_api_key)
else:
    st.warning("OpenAI API key not found. Please set OPENAI_API_KEY in your environment.")
st.set_page_config(
    page_title="World Bank AI Analyzer 🌍",
    page_icon="🌍",
    layout="wide"
)


def add_custom_css():
    st.markdown("""
        <style>
        /* Hide Streamlit default hamburger menu and footer */
        #MainMenu, header, footer {visibility: hidden;}

        /* Set a light background color */
        body {
            background-color: #F9FAFC;
        }

        /* Main container styling */
        .block-container {
            padding: 2rem 2rem 2rem 2rem;
            background-color: #FFFFFF;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0,0,0,0.05);
        }

        /* Heading and text styling */
        h1, h2, h3, h4, h5, h6 {
            color: #212121;
            font-family: "Raleway", sans-serif;
        }

        p, div, label, span {
            color: #424242;
            font-family: "Open Sans", sans-serif;
        }

        /* Expander styling */
        .streamlit-expanderHeader {
            font-weight: 700;
            color: #333333;
        }

        /* Tabs styling */
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

############################################################
# 3. GLOBAL PRICING & UTILITIES
############################################################

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
        return len(text.split())  # Fallback estimate

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



@st.cache_data
def load_dataset():
    """Load the dataset from Hugging Face or any other source."""
    url = "hf://datasets/lukesjordan/worldbank-project-documents/wb_project_documents.jsonl.gz"
    df = pd.read_json(url, lines=True, compression="gzip")
    return df

def get_document_text(df, project_id):
    """Retrieve document text from the dataset by project_id."""
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
            # Assume it's a text file
            return uploaded_file.read().decode("utf-8", errors="replace")
    return None



def analyze_with_gpt(document_text, selected_model, temperature=0.8, max_tokens=2000):
    if client is None:
        return ("Error: OpenAI client not initialized. Please set your API key.", 0, 0, 0, 0, 0)
    instructions = """
You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-10) for each question and provide a detailed analysis to justify your score.
Scoring System:
•	9-10 = Thoroughly Addressed: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question, providing detailed risk mitigation strategies.
•	6-8 = Moderately Addressed: The PAD acknowledges FCV risks and integrates some strategies, but with gaps in specificity or depth.
•	3-5 = Weakly Addressed: The PAD references FCV risks indirectly but lacks substantial integration.
•	0-2 = Not Addressed: No reference to FCV-related risks or considerations.
Output Format:
For each characteristic, provide the following:
1.	Guiding Question: [Question]
o	Analysis: [Detailed analysis of how the PAD addresses the question]
o	Score: [Score between 0 and 10]
At the end, provide:
•	Overall FCV Sensitivity Score: [Sum of scores for all questions]
•	Summary: [Brief summary of the PAD’s FCV sensitivity]
Evaluation Criteria
Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery
1.	Guiding Question: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
o	Analysis: [Your analysis here]
o	Score: [0-10]
2.	Guiding Question: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
o	Analysis: [Your analysis here]
o	Score: [0-10]
Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation
1.	Guiding Question: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
o	Analysis: [Your analysis here]
o	Score: [0-10]
2.	Guiding Question: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
o	Analysis: [Your analysis here]
o	Score: [0-10]
3.	Guiding Question: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
o	Analysis: [Your analysis here]
o	Score: [0-10]
Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding
1.	Guiding Question: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
o	Analysis: [Your analysis here]
o	Score: [0-10]
2.	Guiding Question: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
o	Analysis: [Your analysis here]
o	Score: [0-10]
Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups
1.	Guiding Question: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
o	Analysis: [Your analysis here]
o	Score: [0-10]
2.	Guiding Question: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
o	Analysis: [Your analysis here]
o	Score: [0-10]
Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors
1.	Guiding Question: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
o	Analysis: [Your analysis here]
o	Score: [0-10]
2.	Guiding Question: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
o	Analysis: [Your analysis here]
o	Score: [0-10]
Overall FCV Sensitivity Score
•	Total Score: [Sum of scores for all questions]
•	Summary: [Brief summary of the PAD’s FCV sensitivity, highlighting strengths and weaknesses]


    """
    input_text = instructions + "\n\n" + document_text
    input_tokens = count_tokens(input_text, selected_model)

    try:
        response = client.chat.completions.create(
            model=selected_model,
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": document_text}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        output_text = response.choices[0].message.content
    except Exception as e:
        output_text = f"Error during OpenAI API call: {str(e)}"
    output_tokens = count_tokens(output_text, selected_model)
    input_cost, output_cost, total_cost = calculate_cost(input_tokens, output_tokens, selected_model)

    return output_text, input_tokens, output_tokens, input_cost, output_cost, total_cost


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
    story = []
    for line in lines:
        story.append(Paragraph(line, styles["Normal"]))
    doc.build(story)
    pdf_data = pdf_buffer.getvalue()
    return pdf_data

def export_report_as_csv(response_text):
    lines = response_text.split("\n")
    df = pd.DataFrame({"Analysis": lines})
    return df.to_csv(index=False).encode("utf-8")

def export_report_as_json(response_text):
    lines = response_text.split("\n")
    return json.dumps({"analysis": lines}, indent=2).encode("utf-8")


def chatbot_assistant_ui():
    st.sidebar.subheader("🤖 Chat Assistant")
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    user_query = st.sidebar.text_input("Ask something about the app or OpenAI:", key="assistant_query")
    if st.sidebar.button("Send", key="assistant_send"):
        if user_query and client is not None:
            st.session_state["chat_history"].append({"role": "user", "content": user_query})
            try:
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_query}
                    ],
                    temperature=0.7
                )
                assistant_resp = completion.choices[0].message.content
            except Exception as e:
                assistant_resp = f"Error: {e}"

            st.session_state["chat_history"].append({"role": "assistant", "content": assistant_resp})

    for msg in st.session_state["chat_history"]:
        if msg["role"] == "user":
            st.sidebar.markdown(f"**User**: {msg['content']}")
        else:
            st.sidebar.markdown(f"**Assistant**: {msg['content']}")


def main():
    add_custom_css()
    st.sidebar.title("World Bank AI Analyzer 🌍")
    st.sidebar.markdown("---")
    chatbot_assistant_ui()
    tabs = st.tabs(["Home 🏠", "Analyze Document 📑", "Settings ⚙️", "About ℹ️"])
    with tabs[0]:
        st.title("Welcome to the World Bank AI Analyzer 🌍")
        st.markdown("""
        This application allows you to analyze World Bank project documents using 
        OpenAI models for **Fragility, Conflict, and Violence (FCV)** sensitivity.
        **Key Features**:
        - Project ID or file-based document retrieval
        - GPT-based analysis with cost & token usage tracking
        - Color-coded, collapsible results
        - Exportable AI-generated reports (PDF, CSV, JSON)
        - Chat assistant for quick queries

        Use the tabs above to navigate through the app!
        """)
    with tabs[1]:
        st.header("Analyze Document 📑")
        df = load_dataset()
        analysis_mode = st.radio("Select Analysis Mode:", ["Project ID from Dataset", "Upload Your File"])
        document_text = None
        if analysis_mode == "Project ID from Dataset":
            project_ids = df["project_id"].unique().tolist()
            selected_project_id = st.selectbox("Select or Search Project ID:", project_ids)
            if selected_project_id:
                document_text = get_document_text(df, selected_project_id)
                if document_text:
                    st.subheader("Document Text Preview")
                    st.write(
                        document_text[:500000] + "..."
                        if len(document_text) > 500000
                        else document_text
                    )
                else:
                    st.error("No document found for the selected Project ID.")
        else:
            uploaded_file = st.file_uploader("Upload PDF or Text File", type=["pdf", "txt"])
            if uploaded_file:
                document_text = parse_uploaded_file(uploaded_file)
                if document_text:
                    st.subheader("Uploaded Document Preview")
                    st.write(
                        document_text[:500000] + "..."
                        if len(document_text) > 500000
                        else document_text
                    )
                else:
                    st.error("Could not parse the uploaded file.")

        st.markdown("---")
        if document_text:
            st.subheader("Run Analysis")
            if "selected_model" not in st.session_state:
                st.session_state["selected_model"] = "gpt-4o-mini"
            if "temperature" not in st.session_state:
                st.session_state["temperature"] = 0.8
            if "max_tokens" not in st.session_state:
                st.session_state["max_tokens"] = 2000
            if st.button("🚀 Analyze with GPT"):
                with st.spinner("🤖 AI is analyzing..."):
                    (
                        response_text,
                        input_tokens,
                        output_tokens,
                        input_cost,
                        output_cost,
                        total_cost
                    ) = analyze_with_gpt(
                        document_text,
                        st.session_state["selected_model"],
                        st.session_state["temperature"],
                        st.session_state["max_tokens"]
                    )
                add_usage_history(input_tokens, output_tokens, total_cost)
                st.subheader("Analysis Results")
                color_coded_response = parse_fcv_scores(response_text)
                with st.expander("Click to expand AI Analysis", expanded=True):
                    st.markdown(f"```\n{color_coded_response}\n```")
                st.subheader("📌 Token & Cost Usage")
                st.write(f"**Model Used:** {st.session_state['selected_model']}")
                st.write(f"**Input Tokens:** {input_tokens}")
                st.write(f"**Output Tokens:** {output_tokens}")
                st.write(f"**Total Tokens Used:** {input_tokens + output_tokens}")
                st.subheader("💰 Cost Breakdown")
                st.write(f"**Input Cost:** `${input_cost}`")
                st.write(f"**Output Cost:** `${output_cost}`")
                st.write(f"**Total Cost:** `${total_cost}`")
                st.subheader("📤 Export Analysis")
                st.caption("Use the download buttons below to get your analysis report.")
                pdf_data = export_report_as_pdf(response_text)
                csv_data = export_report_as_csv(response_text)
                json_data = export_report_as_json(response_text)
                st.download_button(
                    label="Download PDF",
                    data=pdf_data,
                    file_name="analysis_report.pdf",
                    mime="application/pdf"
                )
                st.download_button(
                    label="Download CSV",
                    data=csv_data,
                    file_name="analysis_report.csv",
                    mime="text/csv"
                )
                st.download_button(
                    label="Download JSON",
                    data=json_data,
                    file_name="analysis_report.json",
                    mime="application/json"
                )
    with tabs[2]:
        st.header("Settings ⚙️")

        model_options = list(PRICING.keys())
        st.session_state["selected_model"] = st.selectbox(
            "🤖 Select OpenAI Model:",
            model_options,
            index=model_options.index(st.session_state.get("selected_model", "gpt-4o-mini"))
        )
        st.session_state["temperature"] = st.slider(
            "Temperature (creativity)",
            0.0, 1.0,
            st.session_state["temperature"],
            0.1
        )
        st.session_state["max_tokens"] = st.number_input(
            "Max Tokens for Response",
            min_value=100,
            max_value=4000,
            step=100,
            value=st.session_state["max_tokens"]
        )

        st.subheader("Model Pricing (per 1M tokens)")
        price_df = pd.DataFrame(PRICING).T.reset_index().rename(
            columns={"index": "Model", "input": "Input ($)", "output": "Output ($)"}
        )
        st.dataframe(price_df.style.format({"Input ($)": "{:.2f}", "Output ($)": "{:.2f}"}))

        st.subheader("Cost History & Visualization")
        usage_df = get_usage_history_df()
        if not usage_df.empty:
            st.write("Below is the usage history of your analysis sessions.")
            st.dataframe(usage_df)

            c = alt.Chart(usage_df).mark_line(point=True).encode(
                x="timestamp:T",
                y="cost:Q",
                tooltip=["timestamp", "cost"]
            ).properties(title="Cost Over Time")
            st.altair_chart(c, use_container_width=True)

            c2 = alt.Chart(usage_df).mark_bar().encode(
                x="timestamp:T",
                y="total_tokens:Q",
                tooltip=["timestamp", "total_tokens"]
            ).properties(title="Total Tokens Over Time")
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

        **Contact**:
        - Email: example@example.com
        - GitHub: [YourRepo](https://github.com/YourRepo)
        """)


if __name__ == "__main__":
    main()

#will update more changes soon

