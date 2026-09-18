import os

from dotenv import load_dotenv
from google import genai

from retriever import (
    load_documents,
    create_chunks,
    create_embeddings,
    retrieve
)


# -----------------------------
# Load environment variables
# -----------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env"
    )


# -----------------------------
# Create Gemini client
# -----------------------------

client = genai.Client(
    api_key=api_key
)

model = "gemini-3.8-flash"


# -----------------------------
# Main RAG application
# -----------------------------

def main():

    print("\n===== DOCUMENT RAG SYSTEM =====")

    print("\nLoading documents...")

    documents = load_documents()

    if not documents:

        print(
            "\nNo documents found."
            "\nPlease put PDF, TXT, or DOCX files "
            "inside the documents folder."
        )

        return

    print(
        f"Loaded {len(documents)} document sections."
    )

    # -------------------------
    # Create chunks
    # -------------------------

    chunks = create_chunks(documents)

    print(
        f"Created {len(chunks)} document chunks."
    )

    # -------------------------
    # Create embeddings
    # -------------------------

    print("\nCreating document embeddings...")

    embeddings = create_embeddings(chunks)

    print("Embeddings created successfully.")

    # -------------------------
    # Ask question
    # -------------------------

    question = input(
        "\nEnter your question: "
    )

    if not question.strip():

        print("Please enter a question.")

        return

    # -------------------------
    # Retrieve relevant content
    # -------------------------

    print("\nRetrieving relevant content...")

    results = retrieve(
        question,
        chunks,
        embeddings,
        top_k=3
    )

    print("\nRetrieved Sources:")

    for result in results:

        source = result["source"]

        page = result["page"]

        score = result["score"]

        if page:

            print(
                f"- {source} "
                f"(page {page}, "
                f"score: {score:.4f})"
            )

        else:

            print(
                f"- {source} "
                f"(score: {score:.4f})"
            )

    # -------------------------
    # Build context
    # -------------------------

    context_parts = []

    for result in results:

        source = result["source"]

        page = result["page"]

        text = result["text"]

        if page:

            source_info = (
                f"{source}, page {page}"
            )

        else:

            source_info = source

        context_parts.append(
            f"Source: {source_info}\n{text}"
        )

    context = "\n\n".join(context_parts)

    # -------------------------
    # Generate answer
    # -------------------------

    prompt = f"""
You are a document question-answering assistant.

Answer the user's question using ONLY the
retrieved document content provided below.

If the answer cannot be found in the
retrieved content, say:

"I could not find this information
in the provided documents."

Retrieved document content:

{context}

User question:

{question}

Give a clear and concise answer.

Mention the relevant source when appropriate.
"""

    print("\nGenerating answer...")

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    # -------------------------
    # Final answer
    # -------------------------

    print("\n===== FINAL ANSWER =====")

    print(response.text.strip())


if __name__ == "__main__":
    main()