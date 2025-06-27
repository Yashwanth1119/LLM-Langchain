from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
import pinecone, os
from dotenv import load_dotenv

load_dotenv()

def run_query(user_query):
    embeddings = OpenAIEmbeddings()
    pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENV"))
    vectorstore = Pinecone.from_existing_index(index_name=os.getenv("PINECONE_INDEX"), embedding=embeddings)

    llm = ChatOpenAI(temperature=0, model_name="gpt-4")
    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                           retriever=vectorstore.as_retriever(),
                                           return_source_documents=True)

    result = qa_chain({"query": user_query})
    return result['result']
