import os

from dotenv import load_dotenv
from google import genai
from ddgs import DDGS


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.6-flash"


# ============================================================
# AGENT 1 - RESEARCH AGENT
# ============================================================

def research_agent(task, max_results=5):
    """
    Research Agent:
    Searches the web for information related to the task.
    """

    print("\n[Research Agent]")
    print("Searching the web...")

    results = []

    try:
        with DDGS() as ddgs:

            search_results = ddgs.text(
                task,
                max_results=max_results
            )

            for result in search_results:

                results.append({
                    "title": result.get("title", ""),
                    "url": result.get("href", ""),
                    "snippet": result.get("body", "")
                })

    except Exception as e:

        print("Research Agent Error:")
        print(e)

        return []

    print(f"Research Agent found {len(results)} sources.")

    return results


# ============================================================
# AGENT 2 - ANALYST AGENT
# ============================================================

def analyst_agent(task, research_results):
    """
    Analyst Agent:
    Analyzes information collected by the Research Agent.
    """

    print("\n[Analyst Agent]")
    print("Analyzing research findings...")

    if not research_results:
        return "No research information was available."

    research_text = ""

    for index, result in enumerate(
        research_results,
        start=1
    ):

        research_text += f"""
SOURCE {index}

Title:
{result['title']}

URL:
{result['url']}

Information:
{result['snippet']}

----------------------------------------
"""

    prompt = f"""
You are the Analyst Agent in a multi-agent AI system.

The user wants to complete this task:

{task}

The Research Agent collected the following information:

{research_text}

Analyze the collected information.

Your responsibilities:

1. Identify the most important findings.
2. Compare information from different sources.
3. Identify common themes.
4. Identify important differences or limitations.
5. Organize the findings logically.
6. Do not invent information.
7. Use only the information provided by the Research Agent.

Return the analysis in this format:

ANALYSIS

Key Findings:
- ...

Important Observations:
- ...

Comparison:
- ...

Limitations:
- ...

Evidence Sources:
- Source 1
- Source 2
- Source 3
"""

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        print("Analyst Agent Error:")
        print(e)

        return "Analysis could not be generated."


# ============================================================
# AGENT 3 - REPORT AGENT
# ============================================================

def report_agent(task, research_results, analysis):
    """
    Report Agent:
    Combines research and analysis into a final report.
    """

    print("\n[Report Agent]")
    print("Generating final report...")

    references = ""

    for index, result in enumerate(
        research_results,
        start=1
    ):

        references += f"""
[{index}] {result['title']}
URL: {result['url']}
"""

    prompt = f"""
You are the Report Agent in a multi-agent AI system.

The user's task is:

{task}

The Research Agent collected these sources:

{references}

The Analyst Agent produced this analysis:

{analysis}

Create a clear and structured final report.

The report must contain exactly these sections:

1. TITLE

2. TASK

3. EXECUTIVE SUMMARY

4. KEY FINDINGS

5. ANALYSIS

6. CONCLUSION

7. REFERENCES

Requirements:

- Use the research and analysis provided by the other agents.
- Do not invent facts.
- Keep the report clear and professional.
- Use the references supplied by the Research Agent.
- Include source numbers where appropriate.
- Make the report easy to read.
"""

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        print("Report Agent Error:")
        print(e)

        return "Final report could not be generated."