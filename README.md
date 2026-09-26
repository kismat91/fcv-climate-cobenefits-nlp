# FCV Climate Co-benefits NLP

An AI-powered toolkit for analyzing World Bank **Project Appraisal Documents (PADs)** through the lens of the **Fragility, Conflict, and Violence (FCV) Sensitivity Assessment Protocol** — built as a Capstone project with the World Bank's FCV department (George Washington University, MS in Data Science).

The project has two parts:

1. **World Bank AI Analyzer** — a structured, rubric-driven LLM scoring tool that evaluates a PAD against 11 guiding questions across 5 FCV characteristics, with full auditability (cost tracking, exportable reports, reproducible scoring).
2. **PDF Q&A Chatbot** — a retrieval-augmented chatbot for open-ended questions over the same document corpus.

---

## Why this exists

World Bank staff need to assess whether a project's design accounts for how climate action interacts with fragility, conflict, and violence — e.g., does a climate resilience project account for security risks, avoid worsening local tensions, or actively support peacebuilding? Doing this manually for every PAD doesn't scale. This project explores whether an LLM, guided by a carefully specified rubric, can produce consistent, auditable, and defensible FCV-sensitivity scores — plus give analysts a way to ask ad hoc questions across the document corpus.

---

## Part 1 — World Bank AI Analyzer (`app.py`)

A Streamlit application that:

- **Loads a PAD** from one of three sources: a public Hugging Face dataset (`lukesjordan/worldbank-project-documents`), a MongoDB collection of previously scraped/curated documents, or a user-uploaded PDF/text file.
- **Scores the document** against the FCV-Sensitivity Assessment Protocol using an OpenAI model (GPT-4o, GPT-4o-mini, o1, o3-mini), called at `temperature=0` with a fixed `seed` for reproducibility.
- **Parses the model's free-text response** into structured data (`extract_output.py`) — per-question analysis, score, and (where applicable) score probabilities — rather than trusting the model's own formatting.
- **Tracks cost and token usage** per call (via `tiktoken` and a per-model pricing table) and visualizes usage history over time.
- **Exports results** as PDF, CSV, or JSON, with color-coded scores for quick scanning.

### The rubric

The FCV-Sensitivity Assessment Protocol (`prompts.py`) evaluates 5 characteristics:

1. Interactions between climate & FCV affecting program delivery
2. Mitigating the risk of climate actions causing maladaptation
3. Prioritizing climate actions that address FCV root causes & enhance peacebuilding
4. Prioritizing the needs and capacities of vulnerable regions and groups
5. Coordination across development, disaster risk management, and peacebuilding actors

Each characteristic has 2–3 guiding questions (11 total). The repo includes multiple prompt variants that were tested against different scoring scales to calibrate reliability:

- Binary (Yes / Partial / No)
- 0–3 Likert
- 0–10
- 0–100
- Variants that additionally require the model to output a **probability distribution (and log-probabilities) over possible scores**, as an approximation of model confidence per question

### Data pipeline

- `scrapper.py` / `scrapper_new.py` — scrape World Bank project documents
- `filtered_ids.csv` — a curated subset of project IDs the analysis is scoped to
- `pickle_file_extractor.py` — extracts data from serialized scrape output
- `mongo_insert.py` / `mongo_db_check.py` — load/verify PAD text in MongoDB (`projects_db.wb_projects`, keyed by `project_id`, storing full text under `pad_doc`)
- `data_loader.py` — loads the Hugging Face fallback/reference dataset

---

## Part 2 — PDF Q&A Chatbot (`agentic_response.py`)

A lightweight Streamlit chat interface for open-ended questions over the document corpus, built on OpenAI's Responses API with the built-in `file_search` tool against a hosted OpenAI vector store.

**Flow:**

1. Documents are indexed ahead of time into an OpenAI-managed vector store (chunking + embedding handled by OpenAI).
2. At query time, the user's question is embedded and matched against the pre-indexed chunks; the top `max_num_results` (default 5) most relevant chunks are retrieved.
3. Only those retrieved chunks — not the full corpus — are passed to GPT-4o alongside the question.
4. The model generates an answer grounded in the retrieved context, and the response includes a token/cost breakdown.

This is a single-hop retrieve-then-generate pattern: one retrieval, one generation, no query decomposition or iterative retrieval.

---

## Tech stack

| Layer | Tooling |
|---|---|
| UI | Streamlit |
| LLM | OpenAI API (GPT-4o, GPT-4o-mini, o1, o3-mini) |
| Retrieval | OpenAI hosted vector store (`file_search` tool, Responses API) |
| Storage | MongoDB (document corpus) |
| Data source | Hugging Face Datasets (`lukesjordan/worldbank-project-documents`) |
| Parsing | PyPDF2 (PDF ingestion), custom regex-based extractor (`extract_output.py`) |
| Reporting | ReportLab (PDF export), pandas (CSV/JSON export), Altair (usage charts) |
| Token/cost accounting | tiktoken + a per-model pricing table |

---

## Setup

### Prerequisites
- Python 3.9+
- An OpenAI API key
- (Optional) A MongoDB connection string if using the MongoDB data source

### Installation

```bash
git clone https://github.com/kismat91/fcv-climate-cobenefits-nlp.git
cd fcv-climate-cobenefits-nlp
pip install -r requirements.txt
```

### Environment variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key
```

> **Note:** the current codebase has a MongoDB connection string hardcoded in `app.py`. Before deploying or sharing this publicly, move it into an environment variable (e.g. `MONGO_URI`) and rotate the credential.

### Running the apps

```bash
# Rubric-based PAD analyzer
streamlit run app.py

# RAG chatbot over the document corpus
streamlit run agentic_response.py
```

---

## Known limitations / next steps

- **Retrieval** uses OpenAI's managed vector store rather than a self-hosted vector DB (e.g., FAISS, Pinecone, Azure AI Search) — sufficient for a prototype, but doesn't give fine-grained control over chunking, re-ranking, or metadata filtering.
- **No re-ranking or similarity thresholding** on retrieved chunks; `max_num_results` is fixed.
- **Output parsing is regex-based** rather than using structured output (JSON mode / function calling), which is more brittle to prompt format drift.
- **No automated evaluation harness** (e.g., RAGAS, golden-query regression tests, or inter-rater agreement scoring against human-labeled PADs) to track scoring consistency across prompt/model changes.
- **Secrets are hardcoded** in source rather than pulled from a secrets manager.
- **Single-hop RAG only** — no query decomposition, multi-step retrieval, or agentic orchestration.

---

## Project context

Built as a Capstone project in partnership with the World Bank's FCV (Fragility, Conflict, and Violence) department, as part of the MS in Data Science program at The George Washington University.
