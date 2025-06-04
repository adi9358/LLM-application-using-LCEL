import requests
import streamlit as st

API_URL = "https://your-fastapi-server-url/chain"  # Replace with actual deployed FastAPI URL

def get_groq_response(input_text):
    json_body = {
        "text": input_text,
        "language": "english"  # You can modify this as needed
    }
    response = requests.post(API_URL, json=json_body)
    return response.json()

st.title("LLM Q&A Application")
input_text = st.text_input("Ask me anything")

if input_text:
    result = get_groq_response(input_text)
    st.write(result["response"])