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
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from pymongo import MongoClient
from prompts import ALL_PROMPTS
import re

from extract_output import extract_report_content

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = None
if openai_api_key:
    client = OpenAI(api_key=openai_api_key)
else:
    st.warning("OpenAI API key not found. Please set OPENAI_API_KEY in your environment.")

# MongoDB connection
mongo_client = MongoClient(
    'mongodb+srv://Mongo:SecureMongo@cluster0.poitw.mongodb.net/'
    '?retryWrites=true&w=majority&appName=Cluster0&tlsAllowInvalidCertificates=true'
)
db = mongo_client['projects_db']  # Replace with your database name
collection = db['wb_projects']

# Streamlit page config
st.set_page_config(
    page_title="World Bank AI Analyzer 🌍",
    page_icon="🌍",
    layout="wide"
)

############################################################
# 1. CUSTOM CSS
############################################################
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
# 2. GLOBAL PRICING & UTILITIES
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
    """Count tokens in a given text using tiktoken."""
    try:
        enc = tiktoken.encoding_for_model(model)
        return len(enc.encode(text))
    except KeyError:
        # Fallback if the model isn't recognized by tiktoken
        return len(text.split())

def calculate_cost(input_tokens, output_tokens, model):
    """Calculate the cost of a request based on input/output tokens and chosen model."""
    if model in PRICING:
        input_cost_per_million = PRICING[model]["input"]
        output_cost_per_million = PRICING[model]["output"]
        input_cost = (input_tokens / 1_000_000) * input_cost_per_million
        output_cost = (output_tokens / 1_000_000) * output_cost_per_million
        total_cost = input_cost + output_cost
        return round(input_cost, 6), round(output_cost, 6), round(total_cost, 6)
    return 0.0, 0.0, 0.0

def parse_fcv_scores(response_text):
    """
    Parse the FCV scores from the AI response.
    If "Score:" is detected, add a color-coded emoji next to it.
    """
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
                # If score isn't a valid integer, just append the line
                scored_lines.append(line)
        else:
            scored_lines.append(line)
    return "\n".join(scored_lines)

def load_dataset():
    """
    Load the dataset from Hugging Face or any other source.
    This is a placeholder function. Replace with your own dataset if needed.
    """
    url = "hf://datasets/lukesjordan/worldbank-project-documents/wb_project_documents.jsonl.gz"
    df = pd.read_json(url, lines=True, compression="gzip")
    return df

def get_document_text(df, project_id):
    """
    Retrieve document text from the dataset by project_id.
    """
    project_data = df[df["project_id"] == project_id]
    if not project_data.empty:
        return project_data["document_text"].iloc[0]
    else:
        return None

def parse_uploaded_file(uploaded_file):
    """
    Parse text from an uploaded file.
    - If it's a PDF, use PyPDF2 to extract text.
    - Otherwise, assume it's a text file.
    """
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

def analyze_with_gpt(document_text, selected_model, temperature=0.0, max_tokens=3000):
    """
    Analyze the provided document_text using OpenAI GPT, based on the current protocol
    stored in st.session_state["protocol"].
    """
    if client is None:
        return ("Error: OpenAI client not initialized. Please set your API key.", 0, 0, 0, 0, 0)

    protocol_instructions = st.session_state["protocol"]
    input_text = protocol_instructions + "\n\n" + document_text
    input_tokens = count_tokens(input_text, selected_model)

    try:
        response = client.chat.completions.create(
            model=selected_model,
            messages=[
                {"role": "system", "content": protocol_instructions},
                {"role": "user", "content": document_text}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            seed=42
        )
        output_text = response.choices[0].message.content
    except Exception as e:
        output_text = f"Error during OpenAI API call: {str(e)}"

    output_tokens = count_tokens(output_text, selected_model)
    input_cost, output_cost, total_cost = calculate_cost(input_tokens, output_tokens, selected_model)

    return output_text, input_tokens, output_tokens, input_cost, output_cost, total_cost

def add_usage_history(input_tokens, output_tokens, total_cost):
    """
    Save the usage (token count and cost) in the session state for visualization.
    """
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
    """
    Retrieve the usage history as a DataFrame.
    """
    if "usage_history" not in st.session_state:
        st.session_state["usage_history"] = []
    return pd.DataFrame(st.session_state["usage_history"])

def export_report_as_pdf(extracted_results, summary):
    """
    Export the extracted results and total score as a PDF.
    """
    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer)
    styles = getSampleStyleSheet()
    story = []

    def clean_text(text):
        return text.replace("*", "").strip()

    # Add the title & total score
    story.append(Paragraph("Evaluation of the Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol", styles["Heading1"]))
    story.append(Paragraph(f"Total FCV Sensitivity Score: {summary['total_score']}", styles["Heading2"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    # Add the overall summary
    if summary['overall_summary']:
        story.append(Paragraph("<b>Overall Summary:</b>", styles["Heading3"]))
        story.append(Paragraph(clean_text(summary['overall_summary']), styles["Normal"]))
        story.append(Paragraph("<br/>", styles["Normal"]))

    # Add the extracted results
    for characteristic, questions in extracted_results.items():
        story.append(Paragraph(f"Characteristic: {clean_text(characteristic)}", styles["Heading3"]))
        story.append(Paragraph("<br/>", styles["Normal"]))

        for question_data in questions:
            story.append(Paragraph(f"<b>Guiding Question:</b> {clean_text(question_data['question'])}", styles["Normal"]))
            story.append(Paragraph("<br/>", styles["Normal"]))

            story.append(Paragraph(f"<b>Analysis:</b> {clean_text(question_data['analysis'])}", styles["Normal"]))
            story.append(Paragraph("<br/>", styles["Normal"]))

            story.append(Paragraph(f"<b>Score:</b> {question_data['score']}", styles["Normal"]))
            story.append(Paragraph("<br/>", styles["Normal"]))

            probabilities = question_data['probabilities']
            prob_line = ", ".join([f"{score}: {probability:.2f}" for score, probability in probabilities.items()])
            story.append(Paragraph(f"<b>Probabilities:</b> {prob_line}", styles["Normal"]))
            story.append(Paragraph("<br/>", styles["Normal"]))

    # Build the PDF
    doc.build(story)
    pdf_data = pdf_buffer.getvalue()
    pdf_buffer.close()
    return pdf_data

def export_report_as_csv(extracted_results, summary):
    """
    Export the extracted results and total score as a CSV.
    """
    # Prepare data for the CSV
    csv_data = []
    for characteristic, questions in extracted_results.items():
        for question_data in questions:
            csv_data.append({
                "Characteristic": characteristic,
                "Question": question_data["question"],
                "Analysis": question_data["analysis"],
                "Score": question_data["score"],
                "Probabilities": question_data["probabilities"]
            })

    # Add overall summary as a separate row
    if summary['overall_summary']:
        csv_data.append({
            "Characteristic": "Overall Summary",
            "Question": "",
            "Analysis": summary['overall_summary'],
            "Score": "",
            "Probabilities": ""
        })

    # Add total score as a separate row
    csv_data.append({
        "Characteristic": "Total",
        "Question": "",
        "Analysis": "",
        "Score": summary['total_score'],
        "Probabilities": ""
    })

    # Convert to DataFrame
    df = pd.DataFrame(csv_data)

    # Export to CSV
    return df.to_csv(index=False).encode("utf-8")

def export_report_as_json(extracted_results, summary):
    """
    Export the extracted results and total score as a JSON.
    """
    # Prepare the JSON structure
    report_data = {
        "summary": summary,
        "results": extracted_results
    }

    # Convert to JSON string
    return json.dumps(report_data, indent=4).encode("utf-8")

def export_raw_response_as_pdf(raw_response):
    """
    Export the raw response as a PDF with markdown-style formatting.
    """
    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer)
    styles = getSampleStyleSheet()
    story = []

    # Add a title
    story.append(Paragraph("AI Analyzer", styles["Heading1"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    # Add the raw response in markdown-style formatting
    for line in raw_response.splitlines():
        if line.startswith("# "):  # Heading 1
            story.append(Paragraph(line[2:], styles["Heading1"]))
        elif line.startswith("## "):  # Heading 2
            story.append(Paragraph(line[3:], styles["Heading2"]))
        elif line.startswith("### "):  # Heading 3
            story.append(Paragraph(line[4:], styles["Heading3"]))
        elif line.startswith("- "):  # Bullet points
            story.append(Paragraph(f"• {line[2:]}", styles["Normal"]))
        else:  # Regular text
            formatted_line = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", line)
            story.append(Paragraph(formatted_line, styles["Normal"]))
        story.append(Paragraph("<br/>", styles["Normal"]))

    # Build the PDF
    doc.build(story)
    pdf_data = pdf_buffer.getvalue()
    pdf_buffer.close()
    return pdf_data

# Display Extracted Results
def display_extracted_results(extracted_results, summary):
    """
    Display results extracted from the extract_report_content function.
    """

    st.subheader("Extracted Results")
    st.write(f"**Total FCV Sensitivity Score:** {summary['total_score']}")

    # Display the overall summary
    if summary['overall_summary']:
        st.subheader("Overall Summary")
        st.markdown(summary['overall_summary'])

    for characteristic, questions in extracted_results.items():
        with st.expander(f"Characteristic: {characteristic}", expanded=True):
            for question_data in questions:
                st.markdown(f"**Question:** {question_data['question']}")
                st.markdown(f"**Analysis:** {question_data['analysis']}")
                st.markdown(f"**Score:** {question_data['score']}")
                st.markdown(f"**Probabilities:** {question_data['probabilities']}")
                st.markdown("---")

############################################################
# MongoDB Helpers
############################################################
def get_all_project_ids_from_db():
    """
    Return a list of all project IDs from MongoDB.
    """
    docs = collection.find({}, {"project_id": 1})
    project_ids = []
    for d in docs:
        if "project_id" in d:
            project_ids.append(d["project_id"])
    return project_ids

def get_document_text_from_db(project_id):
    """
    Retrieve document text (pad_doc) from MongoDB by project_id.
    """
    doc = collection.find_one({"project_id": project_id})
    if doc:
        return doc.get("pad_doc", "")
    return None

############################################################
# MAIN APP
############################################################
def main():
    add_custom_css()

    # Ensure defaults exist in session
    if "selected_model" not in st.session_state:
        st.session_state["selected_model"] = "gpt-4o-mini"
    if "temperature" not in st.session_state:
        st.session_state["temperature"] = 0.0
    if "max_tokens" not in st.session_state:
        st.session_state["max_tokens"] = 2000

    # Store chosen prompt in session state
    if "selected_prompt" not in st.session_state:
        st.session_state["selected_prompt"] = "Prompt 4 (Probabilities)"  # default is Prompt 4

    st.sidebar.title("World Bank AI Analyzer 🌍")
    st.sidebar.markdown("---")

    # ---------------
    # Prompt Selector
    # ---------------
    prompt_list = list(ALL_PROMPTS.keys())
    default_index = prompt_list.index("Prompt 4 (Probabilities)")  # set Prompt 4 as default
    selected_prompt = st.sidebar.selectbox(
        "Select a Prompt:",
        prompt_list,
        index=default_index
    )
    st.session_state["selected_prompt"] = selected_prompt
    # Set the protocol based on the selected prompt
    st.session_state["protocol"] = ALL_PROMPTS[selected_prompt]

    # ---------------
    # Protocol Editor
    # ---------------
    st.sidebar.subheader("Current Protocol")
    new_protocol = st.sidebar.text_area(
        "Edit or enter a new protocol:",
        st.session_state["protocol"],
        height=400
    )
    if st.sidebar.button("Update Protocol"):
        st.session_state["protocol"] = new_protocol
        st.sidebar.success("Protocol updated successfully!")

    # Main Tabs
    tabs = st.tabs(["Home 🏠", "Analyze Document 📑", "Settings ⚙️", "About ℹ️"])

    #######################
    # TAB 1: Home
    #######################
    with tabs[0]:
        st.title("Welcome to the World Bank AI Analyzer 🌍")
        st.markdown("""
        This application allows you to analyze World Bank project documents using 
        OpenAI models for **Fragility, Conflict, and Violence (FCV)** sensitivity.

        **Key Features**:
        - Multiple data source options (Hugging Face, MongoDB, or your own file)
        - GPT-based analysis with cost & token usage tracking
        - Color-coded, collapsible results
        - Exportable AI-generated reports (PDF, CSV, JSON)

        Use the tabs above to navigate through the app!
        """)

    #######################
    # TAB 2: Analyze Document
    #######################
    with tabs[1]:
        st.header("Analyze Document 📑")
        st.write("Choose your data source, then proceed to load and analyze it.")

        data_source = st.radio(
            "Select Data Source:",
            ["Hugging Face Dataset", "MongoDB Dataset", "Upload Your File"]
        )

        document_text = None

        # =============== Hugging Face Section ===============
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
                    if document_text:
                        st.subheader("Document Text Preview")
                        st.write(
                            document_text[:500000] + "..."
                            if len(document_text) > 500000
                            else document_text
                        )
                    else:
                        st.error("No document found for the selected Project ID.")

        # =============== MongoDB Section ===============
        elif data_source == "MongoDB Dataset":
            if "mongo_ids" not in st.session_state:
                st.session_state["mongo_ids"] = None

            if st.button("Load Project IDs from MongoDB"):
                with st.spinner("Fetching project IDs from MongoDB..."):
                    st.session_state["mongo_ids"] = get_all_project_ids_from_db()
                st.success("MongoDB project IDs loaded.")

            if st.session_state["mongo_ids"]:
                selected_mongo_project_id = st.selectbox(
                    "Select or Search Project ID from MongoDB:",
                    st.session_state["mongo_ids"]
                )
                if selected_mongo_project_id:
                    document_text = get_document_text_from_db(selected_mongo_project_id)
                    if document_text:
                        st.subheader("Document Text Preview")
                        st.write(
                            document_text[:500000] + "..."
                            if len(document_text) > 500000
                            else document_text
                        )
                    else:
                        st.error("No document found for this Project ID in MongoDB.")
            else:
                st.info("Click the button above to load project IDs from MongoDB.")

        # =============== File Upload Section ===============
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

        # If we have text, show the Analyze button
        if document_text:
            st.subheader("Run Analysis")

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

                # Display results
                st.subheader("Analysis Results")
                color_coded_response = parse_fcv_scores(response_text)
                with st.expander("Click to expand AI Analysis", expanded=True):
                    st.markdown(f"```\n{color_coded_response}\n```")

                # Add a download button for the raw response as a PDF
                raw_pdf_data = export_raw_response_as_pdf(response_text)
                st.download_button(
                    label="Download Raw Response as PDF",
                    data=raw_pdf_data,
                    file_name="raw_response.pdf",
                    mime="application/pdf"
                )

                # extract & display results 
                extracted_results, summary = extract_report_content(response_text)
                display_extracted_results(extracted_results, summary)

                # Token and cost breakdown
                st.subheader("📌 Token & Cost Usage")
                st.write(f"**Model Used:** {st.session_state['selected_model']}")
                st.write(f"**Input Tokens:** {input_tokens}")
                st.write(f"**Output Tokens:** {output_tokens}")
                st.write(f"**Total Tokens Used:** {input_tokens + output_tokens}")

                st.subheader("💰 Cost Breakdown")
                st.write(f"**Input Cost:** `${input_cost}`")
                st.write(f"**Output Cost:** `${output_cost}`")
                st.write(f"**Total Cost:** `${total_cost}`")

                # Export options
                st.subheader("📤 Export Analysis")
                st.caption("Use the download buttons below to get your analysis report.")
                pdf_data = export_report_as_pdf(extracted_results, summary)
                csv_data = export_report_as_csv(extracted_results, summary)
                json_data = export_report_as_json(extracted_results, summary)
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

    #######################
    # TAB 3: Settings
    #######################
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

            # Cost over time chart
            c = alt.Chart(usage_df).mark_line(point=True).encode(
                x="timestamp:T",
                y="cost:Q",
                tooltip=["timestamp", "cost"]
            ).properties(title="Cost Over Time")
            st.altair_chart(c, use_container_width=True)

            # Total tokens over time chart
            c2 = alt.Chart(usage_df).mark_bar().encode(
                x="timestamp:T",
                y="total_tokens:Q",
                tooltip=["timestamp", "total_tokens"]
            ).properties(title="Total Tokens Over Time")
            st.altair_chart(c2, use_container_width=True)
        else:
            st.info("No usage history yet.")

    #######################
    # TAB 4: About
    #######################
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

# Launch
if __name__ == "__main__":
    main()
