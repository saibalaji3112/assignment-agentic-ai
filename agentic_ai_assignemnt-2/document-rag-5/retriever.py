import os
import numpy as np

from dotenv import load_dotenv
from pypdf import PdfReader
from docx import Document
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

# -----------------------------
# Load documents
# -----------------------------

def load_documents(folder="documents"):

    documents = []

    for filename in os.listdir(folder):

        path = os.path.join(folder, filename)

        # PDF
        if filename.lower().endswith(".pdf"):

            reader = PdfReader(path)

            for page_number, page in enumerate(reader.pages):

                text = page.extract_text()

                if text and text.strip():

                    documents.append({
                        "source": filename,
                        "page": page_number + 1,
                        "text": text.strip()
                    })

        # TXT
        elif filename.lower().endswith(".txt"):

            with open(path, "r", encoding="utf-8") as file:

                text = file.read()

            if text.strip():

                documents.append({
                    "source": filename,
                    "page": None,
                    "text": text.strip()
                })

        # DOCX
        elif filename.lower().endswith(".docx"):

            doc = Document(path)

            text = "\n".join(
                paragraph.text
                for paragraph in doc.paragraphs
                if paragraph.text.strip()
            )

            if text.strip():

                documents.append({
                    "source": filename,
                    "page": None,
                    "text": text.strip()
                })

    return documents


# -----------------------------
# Split text into chunks
# -----------------------------

def create_chunks(documents, chunk_size=1000):

    chunks = []

    for document in documents:

        text = document["text"]

        for i in range(0, len(text), chunk_size):

            chunk_text = text[i:i + chunk_size]

            if chunk_text.strip():

                chunks.append({
                    "source": document["source"],
                    "page": document["page"],
                    "text": chunk_text.strip()
                })

    return chunks


# -----------------------------
# Create embeddings
# -----------------------------

def create_embeddings(chunks):

    texts = [chunk["text"] for chunk in chunks]

    response = client.models.embed_content(
        model="gemini-embedding-2",
        contents=texts
    )

    embeddings = [
        embedding.values
        for embedding in response.embeddings
    ]

    return np.array(embeddings)


# -----------------------------
# Cosine similarity
# -----------------------------

def cosine_similarity(a, b):

    denominator = (
        np.linalg.norm(a) *
        np.linalg.norm(b)
    )

    if denominator == 0:
        return 0

    return np.dot(a, b) / denominator


# -----------------------------
# Retrieve relevant chunks
# -----------------------------

def retrieve(query, chunks, embeddings, top_k=3):

    query_response = client.models.embed_content(
        model="gemini-embedding-2",
        contents=query
    )

    query_embedding = np.array(
        query_response.embeddings[0].values
    )

    scores = []

    for index, embedding in enumerate(embeddings):

        score = cosine_similarity(
            query_embedding,
            embedding
        )

        scores.append((index, score))

    scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    results = []

    for index, score in scores[:top_k]:

        result = chunks[index].copy()

        result["score"] = score

        results.append(result)

    return results