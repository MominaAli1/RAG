## RAG Pipeline

A lightweight, fully local Retrieval-Augmented Generation (RAG) pipeline built from scratch in Python. Extracts text from a PDF, chunks it, embeds it locally, stores it in a vector database, and answers questions using Groq's LLaMA 3 for generation.

## How it works
```
PDF → Extract → Chunk (200 words) → Embed → Store in Vector DB → Retrieve → Generate Answer
```

1. *Extract* — Pulls raw text from a PDF using PyPDF2
2. *Chunk* — Splits the text into 200-word segments
3. *Embed & Store* — Converts chunks into vectors using a local sentence-transformer model and stores them in ChromaDB
4. *Retrieve* — Finds the most relevant chunks for a given question using vector similarity search
5. *Generate* — Feeds the retrieved chunks + question to Groq's LLaMA 3 model to produce a grounded answer

## Setup

1. Clone the repo
```bash
git clone https://github.com/MominaAli1/RAG.git
cd RAG
```

2. Create and activate a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set your Groq API key
```bash
$env:GROQ_API_KEY="your_groq_key"   # PowerShell
```

5. Run the pipeline
```bash
python main.py
```

## Tech stack

- **PyPDF2** — PDF text extraction
- **sentence-transformers** (`all-MiniLM-L6-v2`) — local embeddings
- **ChromaDB** — vector database
- **Groq (LLaMA 3)** — response generation

## Notes on RAG

RAG grounds an LLM's responses in your own documents, which:
- Eliminates hallucinations by answering only from real source material
- Bypasses the model's knowledge cutoff, since it can reference any document regardless of when it was published
- Improves privacy, since only relevant chunks are sent to the LLM

## Future improvements

- Persistent vector storage (currently resets on every run)
- Overlapping/semantic chunking strategies
- Support for multiple file formats (DOCX, TXT)

## Purpose
This project is part of my journey to become an AI Engineer, focusing on base concepts for now to build production-ready multi-component LLM pipelines and AI agents.

## 📧 Contact
Developed by Momina Ali. For inquiries or collaboration, feel free to connect via GitHub or LinkedIn.
