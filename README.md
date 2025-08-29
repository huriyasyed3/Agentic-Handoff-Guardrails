Multi-Agent Homework Assistant (with Guardrails)

This project is a demo of OpenAI Agents SDK where we use:

Guardrails → to check if the user’s input is actually a homework-related query.

Triage Agent → to decide which specialist agent (Math Tutor / History Tutor) should handle the question.

Default SDK Behavior → if no matching handoff agent is found (e.g., English homework), the Triage Agent itself generates the response.

📌 Features

Homework Guardrail: Blocks inputs that are not related to homework.

Handoff System: Routes questions to either:

📘 History Tutor Agent

➗ Math Tutor Agent

Fallback Behavior: If no suitable handoff exists (like English homework), the Triage Agent answers by itself.

Error Handling: If guardrail blocks input, it raises InputGuardrailTripwireTriggered.

⚙️ How it Works (Flow)

Guardrail Check
Input passes through homework_guardrail.

If is_homework=True → continue.

If is_homework=False → block (Tripwire).

Triage Agent
Decides whether to handoff to:

History Tutor Agent

Math Tutor Agent
or respond itself if no relevant handoff is available.

▶️ Run the Project
# 1. Clone the repo
git clone https://github.com/your-username/Agentic-Handoff-Guardrails.git
cd Agentic-Handoff-Guardrails

# 2. Create virtual environment and install dependencies
uv venv
source .venv/bin/activate   # (or .venv\Scripts\activate on Windows)
pip install -r requirements.txt

# 3. Run the demo
uv run first_agent.py

🧪 Example Outputs
✅ History Homework

Input: For my history homework, tell me about World War 2
Output handled by → History Tutor

✅ Math Homework

Input:My homework: Solve 2x + 5 = 15
Output handled by → Math Tutor

⚠️ English Homework (No Handoff Available)

Input:For my English homework, tell me short intro about William Wordsworth
Output handled by → Triage Agent
(Because no English Tutor Agent is defined, SDK lets the triage agent answer itself.)

📝 Note

Even if no specific agent is available for a handoff,
the SDK’s default design allows the current agent to respond itself.
This ensures the conversation flow continues smoothly, as long as guardrails are satisfied.

🚀 Future Improvements

Add English Tutor Agent for literature/homework queries.

Extend guardrail to detect subject category (Math/History/English/etc.) before routing.

Log blocked inputs for monitoring.



