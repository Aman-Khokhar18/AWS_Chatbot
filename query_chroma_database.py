# query_chroma_database.py

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv('environment.env')

# Constants
CHROMA_PATH = "chroma"

# Prompt Template
PROMPT_TEMPLATE = """

history = {history}

Answer the question based on the context, keep in mind the history provided

{context}

---
You are a AWS documentation assistant, answer the question based on context provided and history: {question}
"""

# Initialize OpenAI API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found in environment variables.")

def load_vector_store():
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    return db


def query_chroma(query_text, history=None, k=4):
    db = load_vector_store()
    results = db.similarity_search_with_relevance_scores(query_text, k=k)

    if len(results) == 0 or results[0][1] < 0.7:
       print(f"Unable to find matching results.")
       return



    # Extract context and sources
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    sources = [doc.metadata.get("source", "Unknown") for doc, _score in results]

    # Prepare the prompt with history
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(history=history, context=context_text, question=query_text)

    model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)


    response_text = model.predict(prompt)
    return response_text
