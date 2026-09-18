# SQL Agent with Tool Use

## 1. Objective

The objective of this project is to develop a **SQL Agent with Tool Use** that can understand natural language questions and interact with a SQLite database.

The agent uses database tools to inspect the database, generate SQL queries, execute them, and provide the final answer to the user.

---

## 2. What is a SQL Agent?

A SQL Agent is an AI-powered system that converts a user's natural language question into a database operation.

Instead of manually writing SQL queries, the user can ask questions such as:

- Show me all employees
- Which employees earn more than 70000?
- Show all products
- Which products have low stock?

The agent determines the appropriate SQL query and uses a database tool to execute it.

---

## 3. ReAct-Based Agent Workflow

This project follows a simple **ReAct-style workflow**:

```text
User Question
      |
      v
Understand Question
      |
      v
Inspect Database Schema
      |
      v
Agent Action
      |
      v
Execute SQL Tool
      |
      v
Tool Observation
      |
      v
Generate Final Answer