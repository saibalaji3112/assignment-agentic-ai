import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)


def generate_answer(question, retrieved_documents):

    context = ""

    for document in retrieved_documents:

        context += f"""
Source: {document['source']}

{document['text']}

--------------------
"""

    prompt = f"""
You are a RAG-based question-answering assistant.

Answer the user's question using ONLY the provided context.

Rules:
1. Do not use outside knowledge.
2. Do not invent information.
3. If the answer is not available in the context, say:
   "I don't have enough information to answer that."
4. Give a clear and concise answer.
5. At the end, mention the source files used.

Context:
{context}

User Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text.strip()