# Multi-Agent Collaboration System

## 1. Objective

The objective of this project is to build a multi-agent AI system in which multiple specialized agents collaborate to automatically complete a given task.

The system contains three specialized agents:

1. Research Agent
2. Analyst Agent
3. Report Agent

Each agent performs a specific responsibility and passes its output to the next agent.

---

## 2. Multi-Agent System

A multi-agent system consists of multiple AI agents that work together to solve a larger task.

Instead of using one AI agent for the entire workflow, the task is divided into specialized responsibilities.

In this project, three agents collaborate to perform research and generate a final report.

---

## 3. Agents

### Research Agent

The Research Agent searches the web for relevant information.

Responsibilities:

- Search for information
- Retrieve multiple sources
- Collect source titles
- Collect source URLs
- Collect relevant snippets

---

### Analyst Agent

The Analyst Agent receives the research results from the Research Agent.

Responsibilities:

- Analyze collected information
- Identify key findings
- Compare information
- Identify common themes
- Identify limitations
- Organize the research findings

---

### Report Agent

The Report Agent receives the research results and analysis.

Responsibilities:

- Combine research and analysis
- Generate an executive summary
- Present key findings
- Generate a conclusion
- Provide references
- Produce the final structured report

---

## 4. Collaboration Workflow

```text
                    User Task
                       |
                       v
              +----------------+
              | Research Agent |
              +----------------+
                       |
                       | Research Results
                       v
              +----------------+
              | Analyst Agent  |
              +----------------+
                       |
                       | Analysis
                       v
              +----------------+
              |  Report Agent  |
              +----------------+
                       |
                       v
                 Final Report