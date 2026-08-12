from retriever import retrieve_documents
from generator import generate_answer


def main():

    print("\n===== RAG QUESTION ANSWERING SYSTEM =====")

    question = input("\nEnter your question: ")

    print("\nRetrieving relevant documents...")

    retrieved_documents = retrieve_documents(
        question,
        top_k=2
    )

    print("\nRetrieved Sources:")

    for document in retrieved_documents:

        print(
            f"- {document['source']} "
            f"(score: {document['score']:.4f})"
        )

    print("\nGenerating answer...")

    answer = generate_answer(
        question,
        retrieved_documents
    )

    print("\nAnswer:")
    print(answer)

    print("\nSource Documents:")

    for document in retrieved_documents:

        print(
            f"- {document['source']}"
        )


if __name__ == "__main__":
    main()