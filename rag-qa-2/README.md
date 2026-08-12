# RAG-Based Question Answering System

## Overview

This project implements a Retrieval-Augmented Generation (RAG) based question answering system.

The system retrieves relevant information from a collection of local text documents and provides the retrieved context to a Large Language Model to generate a grounded answer.

## Architecture

User Question
        |
        v
Question Embedding
        |
        v
Similarity Retrieval
        |
        v
Relevant Documents
        |
        v
Context Construction
        |
        v
Gemini LLM
        |
        v
Final Answer + Sources

## Features

- Local document ingestion
- Text chunking
- Sentence Transformer embeddings
- Local vector indexing
- Cosine similarity retrieval
- Top-K document retrieval
- Context-aware response generation
- Gemini LLM integration
- Source attribution
- Grounded responses
- Protection against unsupported answers

## Technologies Used

- Python
- Sentence Transformers
- NumPy
- Google Gemini API
- python-dotenv
- JSON

## Project Structure

rag-qa/
│
├── documents/
│   ├── college.txt
│   ├── placements.txt
│   └── library.txt
│
├── index.json
├── indexer.py
├── retriever.py
├── generator.py
├── app.py
├── requirements.txt
├── README.md
└── .env

## Workflow

### 1. Document Indexing

The documents inside the `documents` directory are loaded and divided into smaller chunks.

### 2. Embedding Generation

Each document chunk is converted into a numerical embedding using the Sentence Transformer model:

`all-MiniLM-L6-v2`

### 3. Indexing

The text chunks, source names, and embeddings are stored in `index.json`.

### 4. Retrieval

When a user asks a question, the question is converted into an embedding.

Cosine similarity is calculated between the question embedding and stored document embeddings.

The highest-scoring documents are retrieved.

### 5. Response Generation

The retrieved documents are combined into context and passed to Gemini.

The model generates an answer using only the retrieved context.

### 6. Source Attribution

The system displays the documents used to generate the answer.

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv