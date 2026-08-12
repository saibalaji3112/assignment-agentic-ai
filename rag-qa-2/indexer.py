import os
import json
from sentence_transformers import SentenceTransformer


DOCUMENT_FOLDER = "documents"
INDEX_FILE = "index.json"

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_documents():

    documents = []

    for filename in os.listdir(DOCUMENT_FOLDER):

        if filename.endswith(".txt"):

            path = os.path.join(
                DOCUMENT_FOLDER,
                filename
            )

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:

                text = file.read()

            documents.append({
                "source": filename,
                "text": text
            })

    return documents


def create_chunks(text, chunk_size=100):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(
            words[i:i + chunk_size]
        )

        chunks.append(chunk)

    return chunks


def build_index():

    documents = load_documents()

    records = []

    for document in documents:

        chunks = create_chunks(
            document["text"]
        )

        for chunk in chunks:

            records.append({
                "source": document["source"],
                "text": chunk
            })

    texts = [
        record["text"]
        for record in records
    ]

    print("Creating embeddings...")

    embeddings = model.encode(texts)

    index = []

    for record, embedding in zip(
        records,
        embeddings
    ):

        index.append({
            "source": record["source"],
            "text": record["text"],
            "embedding": embedding.tolist()
        })

    with open(
        INDEX_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            index,
            file,
            indent=2
        )

    print("Index created successfully!")
    print(f"Documents indexed: {len(index)}")


if __name__ == "__main__":
    build_index()