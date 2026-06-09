# ✈️ AviateGPT

**Your Personal Local Aviation Brain**

A private, offline AI assistant that answers aviation questions **using only official FAA documents** (FAR/AIM, Pilot’s Handbook of Aeronautical Knowledge, Airplane Flying Handbook, etc.).

It is **not** connected to the internet and does not use generic AI knowledge — it searches your downloaded FAA PDFs and gives grounded, practical answers with source citations.

---

## What This Is For

- Pilots who want accurate, regulation-based answers
- Pre-flight planning and study tool
- Understanding real-world Part 91 operations (especially inoperative equipment like cracked windshields, night currency, weather minimums, etc.)
- A personal knowledge base you fully control

---

## How to Run (Step-by-Step)

### 1. Setup

```powershell
cd E:\aviationbrain

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install streamlit openai chromadb sentence-transformers pypdf
2. Start the LLM Server (in a separate PowerShell window)
PowerShellcd E:\aviationbrain\llama

# Example (adjust model name and -ngl for your GPU)
.\llama-server.exe -m ..\models\Qwen_Qwen3-8B-Q5_K_M.gguf -c 8192 --port 8080 -ngl 25 --threads 20
Keep this window running.
3. Start the Web Interface
In the first window:
PowerShellstreamlit run app.py
This will open AviateGPT in your web browser at:
http://localhost:8501
You can now ask questions like:

"Can I fly with a cracked windshield under Part 91?"
"What are the night currency requirements?"
"Explain 91.155 Class G weather minimums"


Rebuilding the Knowledge Base
PowerShellpython ingest_faraim.py
Run this whenever you add new FAA PDFs or delete the chroma_db folder.

Project Files Overview

app.py → The web interface (Streamlit)
ingest_faraim.py → Loads and processes your FAA PDFs
download_docs.py → Helps download official FAA handbooks
chroma_db/ → The search database (created automatically)


Notes

Everything runs 100% locally on your computer
Works with any GGUF model served on port 8080
First run after changing models may require re-ingestion
License: All Rights Reserved (personal use only)


Made by Jonathan Douglas.
