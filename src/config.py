import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-4")

# Pinecone Configuration
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY", "")
PINECONE_ENV = os.getenv("PINECONE_ENV", "")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX", "")

# App Configuration
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))

# Optional: Fallback or other service config
USE_FAISS = os.getenv("USE_FAISS", "false").lower() == "true"
