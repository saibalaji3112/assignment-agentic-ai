# Text-to-SQL System

## Objective

This project converts natural language questions into SQL queries and executes them on a database.

## Workflow

1. User enters a natural language question.
2. The system analyzes the question.
3. Relevant database schema information is retrieved.
4. An SQL query is generated.
5. The generated SQL query is validated.
6. The query is executed on the database.
7. The final answer is displayed to the user.

## Technologies Used

- Python
- SQLite
- Google Gemini API
- Google GenAI SDK
- python-dotenv

## Project Structure

- `app.py` - Main application
- `answer.py` - Generates the final answer
- `database.py` - Handles database operations
- `retriever.py` - Retrieves relevant database schema
- `validator.py` - Validates generated SQL queries
- `company.db` - SQLite database
- `requirements.txt` - Python dependencies

## How to Run

Install the required dependencies:

```bash
pip install -r requirements.txt