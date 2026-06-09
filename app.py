import streamlit as st
from openai import OpenAI
import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

st.set_page_config(page_title="AviateGPT", page_icon="✈️", layout="wide")
st.title("✈️ AviateGPT")
st.caption("Working RAG Mode")

@st.cache_resource(show_spinner="Loading brain...")
def get_brain():
    client = OpenAI(base_url="http://localhost:8080/v1", api_key="sk-no-key")
    embedder = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
    chroma_client = chromadb.PersistentClient(path="chroma_db")
    collection = chroma_client.get_collection("far_aim")
    return client, embedder, collection

client, embedder, collection = get_brain()

def ask(question):
    # Strong boost for the regulation we care about
    boosted = f"{question} 91.213 inoperative instruments equipment windshield window broken cracked damaged MEL deferral"
    query_embedding = embedder.encode([boosted])[0].tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=15)
    
    contexts = [f"[Source: {m['source']} Page {m['page']}]\n{d.strip()}" 
                for d, m in zip(results["documents"][0], results["metadatas"][0])]
    context = "\n\n".join(contexts)

    prompt = f"""Answer the question using the context if possible. Be accurate and practical about Part 91.

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

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask any aviation question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = ask(prompt)
            st.markdown(answer)
    
    st.session_state.messages.append({"role": "assistant", "content": answer})

st.sidebar.info("Working RAG Mode")