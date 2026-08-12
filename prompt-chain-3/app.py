from chain import (
    extract_key_points,
    create_structured_summary,
    generate_final_summary
)


def main():

    print("\n===== PROMPT CHAINING SUMMARIZATION SYSTEM =====\n")

    text = input("Enter the text to summarize: ")

    if not text.strip():
        print("Please enter some text.")
        return

    print("\nStep 1: Extracting key points...")

    key_points = extract_key_points(text)

    print("\nKey Points:")
    print(key_points)

    print("\nStep 2: Creating structured summary...")

    structured_summary = create_structured_summary(key_points)

    print("\nStructured Summary:")
    print(structured_summary)

    print("\nStep 3: Generating final summary...")

    final_summary = generate_final_summary(structured_summary)

    print("\nFinal Answer:")
    print(final_summary)


if __name__ == "__main__":
    main()