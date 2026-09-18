# Agentic AI Assignment 1

Agentic AI Assignment 1 Questions :-
Q1) Develop a Python program that accepts user input and generates a response using an LLM (OpenAI/Gemini/Ollama). 
Q2) Implement a multi-step LLM workflow to generate a summary, extract key points, and produce three questions from a given topic. 
Q3) Build a simple AI agent that accepts a task, plans the required steps, executes them, and displays the final output. 
Q4) Develop a basic RAG application that retrieves relevant information from a PDF/TXT document and answers user queries using an LLM. 

Agentic AI Assignment 1
This folder contains four Agentic AI projects that demonstrate natural-language database querying, retrieval-augmented generation, prompt chaining, and SQL tool use.
## Projects
| Question | Project | Description |
|----------|---------|-------------|
| Q1 | [Text-to-SQL System](./text-to-sql-1) | Converts natural-language questions into validated SQL queries and executes them on a SQLite database. |
| Q2 | [RAG-Based Question Answering](./rag-qa-2) | Retrieves relevant local documents and uses them as context to generate grounded answers with sources. |
| Q3 | [Prompt Chaining for Summarization](./prompt-chain-3) | Uses a multi-step prompt pipeline to extract key information and produce a final summary. |
| Q4 | [SQL Agent with Tool Use](./sql-agent-4) | Uses a ReAct-style agent workflow to inspect a SQLite database, execute queries, and answer user questions. |

Technologies Used
- Python
- Google Gemini API
- Google GenAI SDK
- SQLite
- Sentence Transformers
- NumPy
- python-dotenv
  
Setup
Each project has its own requirements.txt file.
1. Open the project folder you want to run.
2. Create and activate a virtual environment.
3. Install its dependencies.
4. Add the required API key to a local .env file.
5. Run the project's app.py file.
   
Example:
cd text-to-sql-1
python -m venv .venv
Activate the environment:
.\.venv\Scripts\Activate.ps1
Install dependencies and run:
pip install -r requirements.txt
python app.py
Keep .env, .venv, and __pycache__ files untracked. They should not be committed to GitHub.


## About Each Question
### Q1 – LLM-Based Text-to-SQL Application
This project demonstrates how a Large Language Model can accept a user's natural-language question and generate a useful response. The application uses the Gemini API to understand questions related to company data, generate an SQL query, validate it, execute it on a SQLite database, and display the final answer.
**Project folder:** [text-to-sql-1](./text-to-sql-1)
---

### Q2 – Multi-Step LLM Workflow
This project demonstrates a prompt-chaining workflow. Instead of completing a complex task with one prompt, the task is divided into multiple LLM steps. The system extracts important information from the given text, creates a structured summary, and generates a final response.
**Project folder:** [prompt-chain-3](./prompt-chain-3)
---

### Q3 – AI Agent with Tool Use
This project demonstrates a simple AI agent that accepts a user task and decides which steps are needed to complete it. The SQL agent follows a ReAct-style workflow: it understands the question, inspects the database schema, generates an SQL query, executes the query using database tools, and returns the final result.
**Project folder:** [sql-agent-4](./sql-agent-4)
---

### Q4 – Retrieval-Augmented Generation (RAG) Application
This project demonstrates a RAG-based question-answering system. It retrieves relevant information from local text documents, converts the retrieved content into context, and sends that context to the Gemini LLM to generate a grounded answer. The application also displays the source documents used for the response.
**Project folder:** [rag-qa-2](./rag-qa-2)
