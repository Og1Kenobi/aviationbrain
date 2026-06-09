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
