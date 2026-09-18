# Agentic AI Assignment 2
# Agentic AI Assignment 2

This folder contains four Agentic AI projects that demonstrate document-based RAG, AI research, security log analysis, and multi-agent collaboration.

## Assignment Questions

**Q5)** Build a document-based RAG application that retrieves relevant information from PDF, TXT, or DOCX files and answers user questions using an LLM.

**Q6)** Develop an AI Research Agent that searches for information, summarizes the findings, and generates a structured research report with references.

**Q7)** Build an AI-powered Security Log Analysis Agent that identifies potential threats, classifies their severity, and suggests mitigation steps.

**Q8)** Develop a multi-agent AI system in which specialized agents collaborate to complete a task and generate a final report.

## About Each Question
### Q5 – Document RAG System
This project is a document-based Retrieval-Augmented Generation (RAG) application. It loads PDF, TXT, and DOCX files from the `documents` folder, splits the text into chunks, creates embeddings, retrieves the most relevant content for a user question, and uses Gemini to generate an answer based only on the retrieved context.
The system displays the retrieved sources, including page numbers for PDF documents when available.
**Project folder:** [document-rag-5](./document-rag-5)
---

### Q6 – AI Research Agent
This project demonstrates an AI Research Agent that automates the research process. The agent accepts a research question, searches for relevant information from web sources, collects useful content, summarizes the findings using an LLM, and produces a structured research report with references.
**Project folder:** [research-agent-6](./research-agent-6)
---

### Q7 – Security Log Analysis Agent
This project demonstrates an AI-powered Security Log Analysis Agent. It reads security logs, identifies suspicious events such as failed logins, unauthorized access attempts, suspicious IP addresses, or firewall alerts, and uses an LLM to analyze potential threats.
The final output includes threat detection, severity classification, security analysis, and recommended mitigation actions.
**Project folder:** [security-log-agent-7](./security-log-agent-7)
---

### Q8 – Multi-Agent Collaboration System
This project demonstrates a multi-agent AI system where specialized agents collaborate to complete a larger task.
The system contains three agents:
1. **Research Agent** – Collects relevant information and sources.
2. **Analyst Agent** – Analyzes the research findings and identifies key insights.
3. **Report Agent** – Creates the final structured report with conclusions and references.
**Project folder:** [multi-agent-system-8](./multi-agent-system-8)

## Projects
| Question | Project | Description |
|---|---|---|
| Q5 | [Document RAG System](./document-rag-5) | Retrieves relevant content from local PDF, TXT, or DOCX files and answers questions using Gemini. |
| Q6 | [AI Research Agent](./research-agent-6) | Searches for information, summarizes findings, and prepares a research report with references. |
| Q7 | [Security Log Analysis Agent](./security-log-agent-7) | Analyzes security logs, detects threats, classifies severity, and suggests mitigation steps. |
| Q8 | [Multi-Agent Collaboration System](./multi-agent-system-8) | Uses research, analyst, and report agents to collaborate and produce a final report. |

Technologies Used
- Python
- Google Gemini API
- Google GenAI SDK
- Python dotenv
- NumPy
- PyPDF
- python-docx
- Web search tools or APIs
  
Setup
Each project contains its own requirements.txt file.
1. Open the project folder you want to run.
2. Create and activate a virtual environment.
3. Install the required dependencies.
4. Add the required API key to a local .env file.
5. Run the project's app.py file.
   
Example:
cd document-rag-5
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
Keep .env, .venv, and __pycache__ files untracked. Do not upload API keys or virtual-environment files to GitHub.
