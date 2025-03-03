import os
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key: {api_key[:5]}...")

if not api_key:
    raise ValueError("No se encontro la API key. Verifica tu .env")

class LangChainSetup:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini",
                              temperature=0.7,
                              api_key=api_key)
        self.embeddings = OpenAIEmbeddings(api_key=api_key)
        self.db = Chroma(persist_directory="./chroma_db",
                         embedding_function=self.embeddings)
    
    def get_model(self):
        return self.llm
    
    def get_vector_db(self):
        return self.db
