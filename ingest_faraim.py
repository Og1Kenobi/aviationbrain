from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb
import re
from pathlib import Path

DATA_DIR = Path("data/far_aim")
DB_DIR = Path("chroma_db")
COLLECTION_NAME = "far_aim"

# Good embedding model for technical/regulatory text
EMBED_MODEL = "BAAI/bge-large-en-v1.5"

def load_pdfs():
    texts = []
    for pdf_path in DATA_DIR.glob("*.pdf"):
        print(f"Loading {pdf_path.name}...")
        reader = PdfReader(pdf_path)
        for page_num, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            if text.strip():
                texts.append({
                    "text": text,
                    "source": pdf_path.name,
                    "page": page_num + 1
                })
    return texts

def chunk_text(text, chunk_size=1200, overlap=200):
    """Improved chunking for regulatory text - tries to respect section boundaries"""
    # Try to split on regulation section numbers and headings
    sections = re.split(r'(§\s*\d+\.\d+|\d+\.\d+\s|^\s*[A-Z][A-Za-z\s-]{5,}:|\n\s*[A-Z]{2,})', text, flags=re.MULTILINE)
    
    chunks = []
    current = ""
    for part in sections:
        if len(current) + len(part) > chunk_size and current:
            chunks.append(current.strip())
            current = part
        else:
            current += part
    if current.strip():
        chunks.append(current.strip())
    
    # Fallback to simple overlapping chunks if needed
    if not chunks or max(len(c) for c in chunks) > chunk_size * 2:
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start = end - overlap
    return chunks

def main():
    print("Loading embedding model... (this may take a minute the first time)")
    embedder = SentenceTransformer(EMBED_MODEL)

    print("Loading PDFs...")
    documents = load_pdfs()
    print(f"Loaded {len(documents)} pages from PDFs")

    # Clear old database and create fresh one
    if DB_DIR.exists():
        import shutil
        shutil.rmtree(DB_DIR)
        print("Old database cleared for better chunks.")

    client = chromadb.PersistentClient(path=str(DB_DIR))
    collection = client.get_or_create_collection(COLLECTION_NAME)

    all_chunks = []
    metadatas = []
    ids = []
    chunk_id = 0

    for doc in documents:
        chunks = chunk_text(doc["text"])
        for chunk in chunks:
            all_chunks.append(chunk)
            metadatas.append({
                "source": doc["source"],
                "page": doc["page"]
            })
            ids.append(f"chunk_{chunk_id}")
            chunk_id += 1

    print(f"Created {len(all_chunks)} chunks. Embedding...")

    embeddings = embedder.encode(all_chunks, show_progress_bar=True)

    # Add in safe batches
    print("Adding chunks to database in batches...")
    batch_size = 4000
    total_batches = (len(all_chunks) + batch_size - 1) // batch_size

    for i in range(0, len(all_chunks), batch_size):
        end = i + batch_size
        batch_docs = all_chunks[i:end]
        batch_meta = metadatas[i:end]
        batch_ids = ids[i:end]
        batch_emb = embeddings[i:end].tolist()

        collection.add(
            documents=batch_docs,
            metadatas=batch_meta,
            ids=batch_ids,
            embeddings=batch_emb
        )
        current_batch = (i // batch_size) + 1
        print(f"Added batch {current_batch} / {total_batches}")

    print(f"\n✅ Ingestion complete! Database stored in {DB_DIR}")

if __name__ == "__main__":
    main()