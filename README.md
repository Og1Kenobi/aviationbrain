# ✈️ AviateGPT

**Your Personal Local Aviation Brain**

A private, offline AI assistant that answers aviation questions using **only your downloaded FAA documents** (FAR/AIM, PHAK, Airplane Flying Handbook, etc.).

It is **not** connected to the internet and does not rely on generic AI knowledge — it searches your actual PDFs first.

---

## What is This?

Architecture Overview
This is a RAG (Retrieval-Augmented Generation) system.
#mermaid-diagram-mermaid-mfy0rrh{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#000000;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-diagram-mermaid-mfy0rrh .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-diagram-mermaid-mfy0rrh .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-diagram-mermaid-mfy0rrh .error-icon{fill:#552222;}#mermaid-diagram-mermaid-mfy0rrh .error-text{fill:#552222;stroke:#552222;}#mermaid-diagram-mermaid-mfy0rrh .edge-thickness-normal{stroke-width:1px;}#mermaid-diagram-mermaid-mfy0rrh .edge-thickness-thick{stroke-width:3.5px;}#mermaid-diagram-mermaid-mfy0rrh .edge-pattern-solid{stroke-dasharray:0;}#mermaid-diagram-mermaid-mfy0rrh .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-diagram-mermaid-mfy0rrh .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-diagram-mermaid-mfy0rrh .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-diagram-mermaid-mfy0rrh .marker{fill:#666;stroke:#666;}#mermaid-diagram-mermaid-mfy0rrh .marker.cross{stroke:#666;}#mermaid-diagram-mermaid-mfy0rrh svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#mermaid-diagram-mermaid-mfy0rrh p{margin:0;}#mermaid-diagram-mermaid-mfy0rrh .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#000000;}#mermaid-diagram-mermaid-mfy0rrh .cluster-label text{fill:#333;}#mermaid-diagram-mermaid-mfy0rrh .cluster-label span{color:#333;}#mermaid-diagram-mermaid-mfy0rrh .cluster-label span p{background-color:transparent;}#mermaid-diagram-mermaid-mfy0rrh .label text,#mermaid-diagram-mermaid-mfy0rrh span{fill:#000000;color:#000000;}#mermaid-diagram-mermaid-mfy0rrh .node rect,#mermaid-diagram-mermaid-mfy0rrh .node circle,#mermaid-diagram-mermaid-mfy0rrh .node ellipse,#mermaid-diagram-mermaid-mfy0rrh .node polygon,#mermaid-diagram-mermaid-mfy0rrh .node path{fill:#eee;stroke:#999;stroke-width:1px;}#mermaid-diagram-mermaid-mfy0rrh .rough-node .label text,#mermaid-diagram-mermaid-mfy0rrh .node .label text,#mermaid-diagram-mermaid-mfy0rrh .image-shape .label,#mermaid-diagram-mermaid-mfy0rrh .icon-shape .label{text-anchor:middle;}#mermaid-diagram-mermaid-mfy0rrh .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-diagram-mermaid-mfy0rrh .rough-node .label,#mermaid-diagram-mermaid-mfy0rrh .node .label,#mermaid-diagram-mermaid-mfy0rrh .image-shape .label,#mermaid-diagram-mermaid-mfy0rrh .icon-shape .label{text-align:center;}#mermaid-diagram-mermaid-mfy0rrh .node.clickable{cursor:pointer;}#mermaid-diagram-mermaid-mfy0rrh .root .anchor path{fill:#666!important;stroke-width:0;stroke:#666;}#mermaid-diagram-mermaid-mfy0rrh .arrowheadPath{fill:#333333;}#mermaid-diagram-mermaid-mfy0rrh .edgePath .path{stroke:#666;stroke-width:2.0px;}#mermaid-diagram-mermaid-mfy0rrh .flowchart-link{stroke:#666;fill:none;}#mermaid-diagram-mermaid-mfy0rrh .edgeLabel{background-color:white;text-align:center;}#mermaid-diagram-mermaid-mfy0rrh .edgeLabel p{background-color:white;}#mermaid-diagram-mermaid-mfy0rrh .edgeLabel rect{opacity:0.5;background-color:white;fill:white;}#mermaid-diagram-mermaid-mfy0rrh .labelBkg{background-color:rgba(255, 255, 255, 0.5);}#mermaid-diagram-mermaid-mfy0rrh .cluster rect{fill:hsl(0, 0%, 98.9215686275%);stroke:#707070;stroke-width:1px;}#mermaid-diagram-mermaid-mfy0rrh .cluster text{fill:#333;}#mermaid-diagram-mermaid-mfy0rrh .cluster span{color:#333;}#mermaid-diagram-mermaid-mfy0rrh div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:hsl(-160, 0%, 93.3333333333%);border:1px solid #707070;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-diagram-mermaid-mfy0rrh .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#000000;}#mermaid-diagram-mermaid-mfy0rrh rect.text{fill:none;stroke-width:0;}#mermaid-diagram-mermaid-mfy0rrh .icon-shape,#mermaid-diagram-mermaid-mfy0rrh .image-shape{background-color:white;text-align:center;}#mermaid-diagram-mermaid-mfy0rrh .icon-shape p,#mermaid-diagram-mermaid-mfy0rrh .image-shape p{background-color:white;padding:2px;}#mermaid-diagram-mermaid-mfy0rrh .icon-shape rect,#mermaid-diagram-mermaid-mfy0rrh .image-shape rect{opacity:0.5;background-color:white;fill:white;}#mermaid-diagram-mermaid-mfy0rrh :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}User QuestionRetrievalRelevant FAA Document ChunksAugmented PromptLocal LLM Qwen3-8BCited Answer
How it works:

Your question is converted into a vector
The system finds the most relevant sections from your FAA PDFs
Those sections are sent to the LLM along with your question
The LLM generates an answer grounded in the actual regulations

Components



































ComponentTool UsedPurposeDocumentsFAA PDFsSource of truthEmbeddingsall-MiniLM-L6-v2Converts text to numbers for searchVector DatabaseChromaDBFast similarity searchLLM / Brainllama.cpp + GGUF modelGenerates the final answerWeb InterfaceStreamlitNice chat UI in your browser

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
