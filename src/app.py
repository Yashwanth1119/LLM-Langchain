import streamlit as st
from src.query import run_query

st.title("🧠 GenAI Chat with Your Docs")
query = st.text_input("Ask a question about your data:")

if st.button("Submit") and query:
    response = run_query(query)
    st.write(response)
