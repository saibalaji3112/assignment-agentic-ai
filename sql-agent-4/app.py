import os
from dotenv import load_dotenv
from google import genai

from database import (
    list_tables,
    describe_table,
    execute_sql
)


# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")


# Create Gemini client
client = genai.Client(api_key=api_key)

model = "gemini-3.6-flash"


def run_agent(question):

    print("\n===== SQL AGENT =====")
    print("Question:", question)

    # --------------------------------------------------
    # TOOL 1: List database tables
    # --------------------------------------------------

    tables = list_tables()

    print("\nAvailable tables:")
    print(tables)

    # --------------------------------------------------
    # TOOL 2: Get database schema
    # --------------------------------------------------

    schema = {}

    for table in tables:
        schema[table] = describe_table(table)

    print("\nDatabase schema:")
    print(schema)

    # --------------------------------------------------
    # AGENT: Decide what SQL query to use
    # --------------------------------------------------

    prompt = f"""
You are a SQL Agent that uses database tools.

Database schema:
{schema}

User question:
{question}

Your task:

1. Understand the user's question.
2. Generate a valid SQLite SQL query.
3. Use only the tables and columns provided in the schema.
4. Return ONLY the SQL query.
5. Do not use markdown.
6. Do not explain the query.
"""

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    sql = response.text.strip()

    # Remove markdown code fences if the model adds them
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    print("\nAgent Action:")
    print("execute_sql")

    print("\nGenerated SQL:")
    print(sql)

    # --------------------------------------------------
    # TOOL 3: Execute SQL
    # --------------------------------------------------

    try:

        result = execute_sql(sql)

        print("\nTool Observation:")
        print(result)

    except Exception as e:

        print("\nTool Error:")
        print(e)

        return

    # --------------------------------------------------
    # AGENT: Generate final answer from tool result
    # --------------------------------------------------

    final_prompt = f"""
You are a helpful database assistant.

User question:
{question}

SQL query executed:
{sql}

Database result:
{result}

Give a clear and concise answer to the user's question.

Use only the information contained in the database result.

Do not mention internal implementation details.
"""

    final_response = client.models.generate_content(
        model=model,
        contents=final_prompt
    )

    print("\nFinal Answer:")
    print(final_response.text.strip())


def main():

    print("\n===== SQL AGENT WITH TOOL USE =====")

    question = input("\nEnter your question: ")

    if not question.strip():
        print("Please enter a question.")
        return

    run_agent(question)


if __name__ == "__main__":
    main()