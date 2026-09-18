import os

from dotenv import load_dotenv
from google import genai

from researcher import search_web, format_sources


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.6-flash"


def generate_research_report(question, sources):
    """
    Generate a structured research report using
    the retrieved web information.
    """

    source_text = format_sources(sources)

    prompt = f"""
You are an AI research assistant.

The user has provided the following research question:

{question}

You searched the web and retrieved the following sources:

{source_text}

Using ONLY the information provided in these search results,
create a structured research report.

The report must contain exactly these sections:

1. Research Title
2. Research Question
3. Executive Summary
4. Key Findings
5. Detailed Analysis
6. Conclusion
7. References

Requirements:

- Summarize the information clearly.
- Do not invent facts that are not supported by the sources.
- Use the retrieved sources as evidence.
- Mention relevant source numbers in the report where appropriate.
- Keep the report well structured and readable.
- In the References section, include every source with its title and URL.
- Do not use markdown tables.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()


def main():

    print("\n========================================")
    print("       AI RESEARCH AGENT - Q6")
    print("========================================")

    question = input("\nEnter your research question: ").strip()

    if not question:
        print("\nPlease enter a research question.")
        return

    print("\nSearching the web...")
    
    try:
        sources = search_web(question, max_results=5)
    except Exception as e:
        print("\nSearch Error:")
        print(e)
        return

    if not sources:
        print("\nNo search results were found.")
        return

    print(f"\nFound {len(sources)} sources.")

    print("\nRetrieved Sources:")
    
    for index, source in enumerate(sources, start=1):
        print(f"\n[{index}] {source['title']}")
        print(f"URL: {source['url']}")
        print(f"Snippet: {source['snippet'][:250]}...")

    print("\nGenerating research report...")

    try:
        report = generate_research_report(question, sources)
    except Exception as e:
        print("\nGemini Error:")
        print(e)
        return

    print("\n========================================")
    print("          RESEARCH REPORT")
    print("========================================\n")

    print(report)

    print("\n========================================")
    print("          END OF REPORT")
    print("========================================")


if __name__ == "__main__":
    main()