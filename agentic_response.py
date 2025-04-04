import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Constants for GPT-4o pricing (as of April 2024)
COST_PER_1K_INPUT = 0.005  # USD
COST_PER_1K_OUTPUT = 0.015  # USD

# Your vector store ID
VECTOR_STORE_ID = "vs_67f027885ae08191b8c37ac9c452cb1d"

# Set up Streamlit
st.set_page_config(page_title="PDF Q&A Bot 💬", layout="centered")
st.title("📘 PDF Q&A Chatbot")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Ask a question about the document...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "text": user_input})

    with st.spinner("Thinking..."):
        try:
            # Query OpenAI using file_search
            response = client.responses.create(
                model="gpt-4o",
                input=user_input,
                tools=[{
                    "type": "file_search",
                    "vector_store_ids": [VECTOR_STORE_ID],
                    "max_num_results": 5
                }]
            )

            # Extract answer
            answer = response.output[1].content[0].text

            # Extract usage for cost calculation
            usage = response.usage
            input_tokens = usage.input_tokens
            output_tokens = usage.output_tokens

            # Estimate cost
            input_cost = (input_tokens / 1000) * COST_PER_1K_INPUT
            output_cost = (output_tokens / 1000) * COST_PER_1K_OUTPUT
            total_cost = input_cost + output_cost

            answer += f"\n\n---\n🧮 **Usage Summary**\n- Input tokens: `{input_tokens}`\n- Output tokens: `{output_tokens}`\n- 💰 Estimated cost: `${total_cost:.5f}`"

        except Exception as e:
            answer = f"❌ Error: {e}"

    st.session_state.chat_history.append({"role": "assistant", "text": answer})

# Display full chat
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])
