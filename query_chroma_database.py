from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os


load_dotenv('environment.env')


CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Below is the conversation history:

{history}

--- 

Based on the provided context, answer the user's question in detail.

Context:
{context}

Question: {question}
"""

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found in environment variables.")

def load_vector_store():
    """Loads the Chroma vector store with OpenAI embeddings."""
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    return db

def query_chroma(query_text, history=None, k=4):
    """Queries the Chroma vector store and returns a response."""
    db = load_vector_store()
    results = db.similarity_search_with_relevance_scores(query_text, k=k)

    if len(results) == 0 or results[0][1] < 0.7:
        print("Unable to find matching results.")
        return None

    context_text = "\n\n---\n\n".join([doc.page_content[:500] for doc, _ in results])
    sources = [doc.metadata.get("source", "Unknown") for doc, _ in results]

    history = history or "No history available."
    formatted_history = f"User: {history}\n"

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(history=formatted_history, context=context_text, question=query_text)
    model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.5)
    response_text = model.predict(prompt)
    return response_text


