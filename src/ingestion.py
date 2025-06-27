from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone
import os
from dotenv import load_dotenv
from config import OPENAI_API_KEY, PINECONE_API_KEY, PINECONE_ENV, PINECONE_INDEX_NAME


load_dotenv()

def ingest_data(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENV"))

    Pinecone.from_documents(documents=chunks,
                            embedding=embeddings,
                            index_name=os.getenv("PINECONE_INDEX"))

if __name__ == "__main__":
    ingest_data("data/sample.pdf")
