import streamlit as st
import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)


@st.cache_data
def load_dataset():
    url = "hf://datasets/lukesjordan/worldbank-project-documents/wb_project_documents.jsonl.gz"
    df = pd.read_json(url, lines=True, compression="gzip")
    return df

def get_document_text(df, project_id):
    project_data = df[df["project_id"] == project_id]
    if not project_data.empty:
        return project_data["document_text"].iloc[0]  # Assuming 'document_text' contains the text
    else:
        return None

def analyze_with_gpt(document_text):
    instructions = """
    You are an expert in Fragility, Conflict, and Violence (FCV) Sensitivity Assessment. Your task is to evaluate a Project Appraisal Document (PAD) based on the FCV-Sensitivity Assessment Protocol. Analyze the provided document text and answer the following guiding questions for each of the five characteristics. Assign a score (0-3) for each question and provide a detailed analysis to justify your score.
### Scoring System:
- **3 = Thoroughly Addressed**: The PAD explicitly and comprehensively incorporates FCV-sensitive measures aligned with the question.
- **2 = Moderately Addressed**: The PAD adequately addresses the question but may lack depth or completeness.
- **1 = Weakly Addressed**: The PAD references the issue but in a limited, superficial, or indirect way.
- **0 = Not Addressed**: There is no evidence in the PAD that the issue has been addressed.

### Output Format:
For each characteristic, provide the following:
1. **Guiding Question**: [Question]
   - **Analysis**: [Detailed analysis of how the PAD addresses the question]
   - **Score**: [Score between 0 and 3]

At the end, provide:
- **Overall FCV Sensitivity Score**: [Sum of scores for all questions]
- **Summary**: [Brief summary of the PAD's FCV sensitivity]

---

### Characteristic 1: Consider How Interactions Between Climate & FCV Affect Program Delivery
1. **Guiding Question**: Does the PAD explicitly identify risks to project implementation from FCV-related barriers (e.g., security risks, institutional weaknesses, or strained community relations)?
   - **Analysis**: [Your analysis here]
   - **Score**: [0-3]

2. **Guiding Question**: To what extent does the PAD seek to identify the specific pathways through which climate impacts interact with FCV dynamics?
   - **Analysis**: [Your analysis here]
   - **Score**: [0-3]

---

### Characteristic 2: Mitigate the Risk of Climate Actions Resulting in Maladaptation
1. **Guiding Question**: Does the PAD incorporate specific safeguards to ensure project interventions do not exacerbate FCV-related vulnerabilities or create new sources of tension?
   - **Analysis**: [Your analysis here]
   - **Score**: [0-3]

2. **Guiding Question**: To what extent are adaptive mechanisms embedded into the project to accommodate evolving FCV conditions in the country or region?
   - **Analysis**: [Your analysis here]
   - **Score**: [0-3]

3. **Guiding Question**: Does the PAD show evidence of explicit efforts to balance immediate needs with long-term resilience-building in a way that avoids maladaptive outcomes?
   - **Analysis**: [Your analysis here]
   - **Score**: [0-3]

---

### Characteristic 3: Prioritize Climate Actions That Address FCV Root Causes & Enhance Peacebuilding
1. **Guiding Question**: Does the PAD include interventions that explicitly address root causes of FCV, such as inequitable access to resources or weak governance?
   - **Analysis**: [Your analysis here]
   - **Score**: [0-3]

2. **Guiding Question**: Does the project actively seek to promote peacebuilding, such as fostering trust, social cohesion, or conflict resolution?
   - **Analysis**: [Your analysis here]
   - **Score**: [0-3]

---

### Characteristic 4: Prioritize the Needs and Capacities of Vulnerable Regions and Groups
1. **Guiding Question**: Does the PAD explicitly identify vulnerable populations (e.g., women, displaced persons, minorities) and include measures to address their specific needs?
   - **Analysis**: [Your analysis here]
   - **Score**: [0-3]

2. **Guiding Question**: Are mechanisms included to ensure equitable benefit-sharing and avoid reinforcing inequalities?
   - **Analysis**: [Your analysis here]
   - **Score**: [0-3]

---

### Characteristic 5: Encourage Coordination Across Development, DRM, & Peacebuilding Actors
1. **Guiding Question**: Does the PAD demonstrate evidence of active collaboration with stakeholders across sectors (e.g., humanitarian, peacebuilding, disaster risk management)?
   - **Analysis**: [Your analysis here]
   - **Score**: [0-3]

2. **Guiding Question**: Does the PAD outline mechanisms to align actions, resolve mandate overlaps, and avoid duplication across relevant actors?
   - **Analysis**: [Your analysis here]
   - **Score**: [0-3]

---

### Overall FCV Sensitivity Score
- **Total Score**: [Sum of scores for all questions]
- **Summary**: [Brief summary of the PAD's FCV sensitivity, highlighting strengths and weaknesses]
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": document_text}
        ],
        temperature=0.8,
        max_tokens=4000
    )
    return response.choices[0].message.content

def main():
    st.title("Project Document Analyzer")
    df = load_dataset()
    project_id = st.text_input("Enter Project ID:")
    if project_id:
        document_text = get_document_text(df, project_id)
        if document_text:
            st.subheader("Document Text")
            st.write(document_text)
            if st.button("Analyze"):
                with st.spinner("Analyzing..."):
                    result = analyze_with_gpt(document_text)
                st.subheader("Analysis Results")
                st.write(result)
        else:
            st.error("No document found for the given Project ID.")
if __name__ == "__main__":
    main()