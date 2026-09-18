import json
import numpy as np
from sentence_transformers import SentenceTransformer


INDEX_FILE = "index.json"

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_index():

    with open(
        INDEX_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def retrieve_documents(question, top_k=2):

    index = load_index()

    question_embedding = model.encode(
        question
    )

    results = []

    for item in index:

        document_embedding = np.array(
            item["embedding"]
        )

        similarity = np.dot(
            question_embedding,
            document_embedding
        ) / (
            np.linalg.norm(question_embedding)
            *
            np.linalg.norm(document_embedding)
        )

        results.append({
            "source": item["source"],
            "text": item["text"],
            "score": float(similarity)
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results[:top_k]


if __name__ == "__main__":

    question = input(
        "Enter your question: "
    )

    results = retrieve_documents(question)

    print("\nRetrieved Documents:\n")

    for result in results:

        print(
            f"Source: {result['source']}"
        )

        print(
            f"Score: {result['score']:.4f}"
        )

        print(
            result["text"]
        )

        print("-" * 50)