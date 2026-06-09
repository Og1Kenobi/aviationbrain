# ✈️ AviateGPT

**Your Personal Local Aviation Brain**

A private, offline AI assistant that answers aviation questions using **only your downloaded FAA documents** (FAR/AIM, PHAK, Airplane Flying Handbook, etc.).

It is **not** connected to the internet and does not rely on generic AI knowledge — it searches your actual PDFs first.

---

## What is This?

This is a **RAG AI** (Retrieval-Augmented Generation).

### Architecture Overview
User Question
↓
[Retrieval] → Searches your FAA PDFs using smart embeddings
↓
Relevant Chunks (with page numbers)
↓
[Augmented Prompt] → Sent to Local LLM
↓
LLM generates accurate, cited answer
text| Component              | Tool Used                  | Purpose |
|------------------------|----------------------------|-------|
| Documents              | FAA PDFs                   | Source of truth |
| Embeddings             | all-MiniLM-L6-v2           | Converts text to searchable vectors |
| Vector Database        | ChromaDB                   | Fast similarity search |
| LLM (The Brain)        | llama.cpp + GGUF model     | Generates the final answer |
| Web Interface          | Streamlit                  | Chat UI in your browser |

This architecture makes the AI much more accurate and trustworthy for aviation regulations.

---

## How to Run (Step-by-Step)

### 1. Setup

```powershell
cd E:\aviationbrain

python -m venv venv
venv\Scripts\activate

pip install --upgrade pip
pip install streamlit openai chromadb sentence-transformers pypdf
2. Start LLM Server (separate window)
PowerShellcd E:\aviationbrain\llama

.\llama-server.exe -m ..\models\Qwen_Qwen3-8B-Q5_K_M.gguf -c 8192 --port 8080 -ngl 25 --threads 20
3. Start the App
PowerShellstreamlit run app.py
Open http://localhost:8501 in your browser.

Rebuilding the Knowledge Base
PowerShellpython ingest_faraim.py

Notes

Everything runs 100% locally
Works with any GGUF model
License: All Rights Reserved (personal use only)


Made by Jonathan Douglas.
