import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_key_points(text):
    prompt = f"""
You are the first stage of a summarization pipeline.

Read the following text and extract only the most important
facts, ideas, and information.

Do not write a final summary yet.

TEXT:
{text}

Return the important points as a clear numbered list.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text.strip()


def create_structured_summary(key_points):
    prompt = f"""
You are the second stage of a summarization pipeline.

Organize the following key points into a structured summary.

Group related information together.
Remove repetition.
Keep important details.

KEY POINTS:
{key_points}

Return a well-organized summary.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text.strip()


def generate_final_summary(structured_summary):
    prompt = f"""
You are the final stage of a summarization pipeline.

Create a concise and easy-to-understand final summary
from the structured summary below.

Keep only the most important information.
Use simple language.
Do not add information that is not present in the input.

STRUCTURED SUMMARY:
{structured_summary}

Return only the final summary.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text.strip()