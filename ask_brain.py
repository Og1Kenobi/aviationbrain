import streamlit as st
from openai import OpenAI
import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

# ==================== CONFIG ====================
LLM_URL = "http://localhost:8080/v1"
EMBED_MODEL = "BAAI/bge-large-en-v1.5"
DB_DIR = Path("chroma_db")
COLLECTION_NAME = "far_aim"

@st.cache_resource
def load_components():
    client = OpenAI(base_url=LLM_URL, api_key="sk-no-key")
    embedder = SentenceTransformer(EMBED_MODEL)
    chroma_client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = chroma_client.get_collection(COLLECTION_NAME)
    return client, embedder, collection

client, embedder, collection = load_components()

def retrieve_context(question, top_k=15):
    query_embedding = embedder.encode([question])[0].tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    contexts = [f"[Source: {meta['source']} Page {meta['page']}]\n{doc.strip()}" 
                for doc, meta in zip(results["documents"][0], results["metadatas"][0])]
    return "\n\n".join(contexts)

def ask(question):
    context = retrieve_context(question)
    
    prompt = f"""You are an extremely strict and precise FAA Part 91 airworthiness expert.

CRITICAL INSTRUCTIONS:
- ONLY answer using information actually present in the provided context.
- If the context contains any relevant regulation or text, quote or closely paraphrase it and ALWAYS include the source and page number.
- If the context has **no relevant information**, respond with **exactly**:  
  "**Note:** I don't have specific information on this topic in the loaded FAA documents."

Do not add general safety opinions. Do not assume. Be legalistic and accurate.

Context:
{context}

Question: {question}

Answer:"""

    response = client.chat.completions.create(
        model="local-model",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=1500
    )
    return response.choices[0].message.content

# ===================== UI =====================
st.set_page_config(page_title="AviateGPT", page_icon="✈️", layout="wide")
st.title("✈️ AviateGPT")
st.caption("Local FAA Documents • Strict RAG Mode")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask any aviation question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ask(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

st.sidebar.header("About")
st.sidebar.info("Fully local system using your FAR/AIM + FAA Handbooks.\nStrict document-only mode.")
st.sidebar.caption("Qwen3-8B + llama.cpp")