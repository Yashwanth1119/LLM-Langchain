# LLM-Langchain
# 🧠 LLM Langchain Chatbot with Pinecone

This is a GenAI project using LangChain, OpenAI, and Pinecone to build a chatbot or question-answering system over your documents.

## 🔧 Features

- Upload PDFs or text
- Chunk, embed, and store with Pinecone
- Query using GPT-4 via LangChain
- Deployable via Docker

## 🚀 Quickstart

```bash
pip install -r requirements.txt
python src/ingestion.py
streamlit run src/app.py
