import sqlite3
import os
from dotenv import load_dotenv
from retriever import retrieve_relevant_schema, format_schema
import google.generativeai as genai
from validator import validate_sql
from answer import generate_answer

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_sql(question, schema):

    prompt = f"""
You are a Text-to-SQL system.

Convert the user's question into SQLite SQL.

Database schema:

{schema}

Rules:
- Return ONLY SQL.
- Do not use markdown.
- Do not explain anything.
- Use only tables and columns from the schema.
- Generate valid SQLite SQL.

User question:

{question}
"""

    response = model.generate_content(prompt)

    sql = response.text.strip()

    # Remove markdown if Gemini returns it
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()


def execute_sql(sql):

    conn = sqlite3.connect("company.db")

    cursor = conn.cursor()

    try:

        cursor.execute(sql)

        rows = cursor.fetchall()

        if cursor.description:

            columns = [
                description[0]
                for description in cursor.description
            ]

            result = []

            for row in rows:

                result.append(
                    dict(zip(columns, row))
                )

            return result

        return "Query executed successfully."

    except Exception as e:

        return f"SQL Error: {e}"

    finally:

        conn.close()


def main():

    print("\n===== TEXT TO SQL SYSTEM =====")

    question = input("\nEnter your question: ")

    relevant_schema = retrieve_relevant_schema(question)

    schema = format_schema(relevant_schema)

    print("\nRetrieved Schema:")
    print(schema)

    print("\nGenerating SQL...")

    sql = generate_sql(question, schema)

    print("\nGenerated SQL:")
    print(sql)

    print("\nValidating SQL...")

    is_valid, message = validate_sql(sql)

    if not is_valid:

        print("SQL Validation Failed!")
        print(message)
        return

    print("SQL Validation Passed!")

    print("\nExecuting SQL...")

    result = execute_sql(sql)

    print("\nResult:")
    print(result)

    print("\nFinal Answer:")
    answer = generate_answer(question, result)

    print(answer)


if __name__ == "__main__":
    main()