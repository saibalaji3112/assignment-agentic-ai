import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.6-flash"


def analyze_security_logs(logs):
    """
    Analyze security logs using an AI security agent.
    """

    prompt = f"""
You are an AI Security Log Analysis Agent.

Your task is to analyze the security logs provided below.

SECURITY LOGS:

{logs}

Perform the following tasks:

1. Identify suspicious or potentially malicious events.
2. Identify possible security threats.
3. Classify each significant threat using one of these severity levels:
   - LOW
   - MEDIUM
   - HIGH
   - CRITICAL
4. Explain why each event is considered suspicious.
5. Suggest practical mitigation steps.
6. Identify affected users, services, IP addresses, or resources when available.
7. Provide an overall security assessment.

Important rules:

- Base your analysis only on the provided logs.
- Do not invent events or information.
- Treat IP addresses and log entries as evidence, not proof of malicious intent.
- Do not claim that an attack is confirmed unless the logs provide sufficient evidence.
- Do not execute any commands or security actions.
- Provide recommendations only.

Return the result using exactly this structure:

SECURITY ANALYSIS REPORT

1. EXECUTIVE SUMMARY

2. DETECTED THREATS

For each threat include:

Threat:
Severity:
Evidence:
Affected Resource:
Explanation:

3. SEVERITY SUMMARY

LOW:
MEDIUM:
HIGH:
CRITICAL:

4. MITIGATION STEPS

For each significant threat provide practical mitigation steps.

5. OVERALL SECURITY ASSESSMENT

Provide a concise overall assessment based only on the supplied logs.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()