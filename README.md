# ✈️ AviateGPT

**Your Personal Local Aviation Brain**

A private, offline AI assistant that answers aviation questions using **only your downloaded FAA documents** (FAR/AIM, PHAK, Airplane Flying Handbook, etc.).

It does **not** use generic internet AI knowledge — it searches your actual PDFs and gives practical, cited answers.

---

## What is Streamlit?

**Streamlit** is a simple tool that turns Python code into a nice web app.  
In this project, Streamlit creates the chat interface you see in your browser (`http://localhost:8501`). It’s lightweight and runs entirely on your computer.

---

## How to Run (Step-by-Step)

### 1. Setup

Open PowerShell and run:

```powershell
cd E:\aviationbrain

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies (including Streamlit)
pip install --upgrade pip
pip install streamlit openai chromadb sentence-transformers pypdf
2. Start the LLM Server (separate PowerShell window)
PowerShellcd E:\aviationbrain\llama

# Example command - adjust as needed for your model/GPU
.\llama-server.exe -m ..\models\Qwen_Qwen3-8B-Q5_K_M.gguf -c 8192 --port 8080 -ngl 25 --threads 20
Keep this window open.
3. Start AviateGPT (Streamlit Web Interface)
In the first PowerShell window:
PowerShellstreamlit run app.py
This will automatically open AviateGPT in your web browser at:
http://localhost:8501

Rebuilding the Knowledge Base
PowerShellpython ingest_faraim.py
Run this if you add new PDFs or delete the chroma_db folder.

Simple Architecture Explanation
Here's how your AviateGPT actually works:
textUser Question
      ↓
[Retrieval] → Searches your FAA PDFs using embeddings (vector similarity)
      ↓
Relevant Chunks (with page numbers) 
      ↓
[Augmented Prompt] → Sent to the Local LLM (Qwen3-8B, etc.)
      ↓
LLM generates answer based ONLY on your documents + general knowledge
      ↓
Answer with citations
Full Architecture Breakdown















































ComponentWhat it isTool UsedPurposeDocumentsFAA PDFs (FAR/AIM, PHAK, etc.)Your data/far_aim/ folderSource of truthEmbedding ModelConverts text to numbersall-MiniLM-L6-v2Creates searchable vectorsVector DatabaseStores embeddingsChromaDBFast similarity searchLLM / BrainThe actual AI that talksllama.cpp + GGUF modelGenerates the final answerWeb InterfaceThe chat window you seeStreamlitUser-friendly frontendServerConnects everythingOpenAI-compatible APIGlue between components
Why This is Good

Grounded — It tries to answer from your real FAA documents first
Private — Nothing leaves your computer
Customizable — You control the documents and the model
Explainable — It can show you the source pages

Notes

Everything runs 100% locally on your machine
You can use any GGUF model by changing the server command
Streamlit is only used to create the chat interface — no data is sent over the internet


Made by Jonathan Douglas.
