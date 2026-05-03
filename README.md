# Astro RAG Project

Production-style Vedic Astrology RAG (Retrieval-Augmented Generation) system.

This system converts astrology knowledge into structured data and retrieves accurate answers using metadata + semantic search.

---

## Features (Current)

- Text cleaning pipeline
- Paragraph-based chunking (domain-aware)
- Metadata enrichment (planet, house, topics)
- Embedding generation (sentence-transformers)
- Metadata search
- Semantic search (cosine similarity)
- Hybrid retrieval (metadata + embeddings)
- Template-based answer generation (no hallucination)

---

## Project Structure

astro_rag/
│
├── app/
│   ├── ingestion/
│   ├── embeddings/
│   ├── rag/
│   ├── guardrails/
│   └── api/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── tests/
├── requirements.txt
├── requirements-core.txt
└── README.md

---

## Prerequisites

- Python 3.10+
- PowerShell / Terminal
- VS Code (recommended)

---

## Setup

cd C:\Users\tanuj\Desktop\RAG_Project\astro_rag

python -m venv .venv
.venv\Scripts\Activate.ps1

pip install -r requirements-core.txt

---

## How to Run (Step-by-Step)

### 1. Activate Virtual Environment

.venv\Scripts\Activate.ps1

---

### 2. Run Ingestion (Create Chunks)

python -m app.ingestion.run_pipeline

---

### 3. Generate Embeddings

python -m app.embeddings.embed_chunks

---

### 4. Test Metadata Search

python -m app.rag.metadata_search

---

### 5. Test Semantic Search

python -m app.rag.semantic_search

---

### 6. Test Hybrid Retrieval

python -m app.rag.hybrid_retriever

---

### 7. Generate Answer

python -m app.rag.answer_generator

---

## Current System Flow

Raw Text → Clean Text → Paragraph Chunking → Metadata Enrichment → Embeddings → Hybrid Retrieval → Answer Generation

---

## Key Design Principles

1. Metadata-first retrieval  
2. Domain-aware chunking  
3. Hybrid search  
4. Deterministic outputs (v1)

---

## Example Query

mars in 11th house gains through friends

---

## Next Steps (Planned)

- Add Qdrant vector database
- Add FastAPI endpoints
- Add LLM (Ollama/OpenAI)
- Add guardrails
- Add evaluation pipeline
- Improve metadata extraction
- Add chart-based reasoning

---

## Goal

Build a production-grade, explainable astrology AI system.

---

## Status

RAG Foundation Complete  
Production Layer Pending
