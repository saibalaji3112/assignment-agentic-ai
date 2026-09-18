# Document RAG Agent

## 1. Objective

The objective of this project is to build an AI-powered Document Retrieval-Augmented Generation (RAG) system that can read documents, retrieve relevant content, and answer user questions using an LLM.

The system supports PDF, TXT, and DOCX documents.

Instead of providing the entire document to the language model, the system extracts the document content, divides it into smaller chunks, creates embeddings, retrieves the most relevant chunks, and uses the retrieved information to generate the final answer.

---

## 2. What is Document RAG?

Retrieval-Augmented Generation (RAG) is a technique that combines information retrieval with a Large Language Model (LLM).

The system first retrieves relevant information from the provided documents and then gives that information to the LLM to generate an answer.

This helps the model answer questions using information from the user's documents.

---

## 3. Workflow

```text
PDF / TXT / DOCX
       |
       v
Document Loader
       |
       v
Text Extraction
       |
       v
Text Chunking
       |
       v
Document Embeddings
       |
       v
Vector Similarity Search
       |
       v
Relevant Content
       |
       v
Gemini LLM
       |
       v
Final Answer
