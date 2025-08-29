from agents import Agent , Runner ,GuardrailFunctionOutput, InputGuardrail ,InputGuardrailTripwireTriggered
from dotenv import load_dotenv
import asyncio
from pydantic import BaseModel

load_dotenv()


class HomeWorkOutput(BaseModel):
    is_homework:bool
    reasoning:str

guradrail_agent=Agent(
    name="Guardrail Check",
    instructions="check if the user is asking about homework.",
    output_type= HomeWorkOutput
)

history_tutor_agent = Agent(
    name = "History Tutor",
    handoff_description ="Specialist agent for historical Questions",
    instructions="you provide assistant with historical quries.Explain important events and context clearly."
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist Agent for math questions.",
    instructions="you provide help with math problems. Explain your reasoning at each step and include examples."
)
async def homework_guardrail(ctx, agent, input_data):
      result = await Runner.run(guradrail_agent , input_data , context=ctx.context)
      final_output = result.final_output_as(HomeWorkOutput)
      return GuardrailFunctionOutput(
        output_info =  final_output,
        tripwire_triggered = not final_output.is_homework,
      )
triage_agent=Agent(
    name="Triage Agent",
    instructions="you determine which agent to use based on the user's homework questions.",
    handoffs = [ history_tutor_agent, math_tutor_agent ],
    input_guardrails=[
        InputGuardrail(guardrail_function=homework_guardrail),
    ],
)

async def main():
        # Example 1: History question
     try:
         result = await  Runner.run(triage_agent ,input="For my history homework, tell me about World War 2")
         print(result.final_output)
         print(result.last_agent.name)
     except InputGuardrailTripwireTriggered as e:
          print("Guardrail 1 block  this input:", e)
    
    #example 2 :
    # Note:
# Even if no specific agent is available for a handoff, 
# the SDK’s default design allows the current agent to respond itself. 
# This means that as long as at least one guardrail is followed, 
# the system ensures the conversation flow continues smoothly.

     try:
        result = await Runner.run(triage_agent , input="For my english homework, tell me short intro about  William Wordsworth")
        print(result.final_output)
        print(result.last_agent.name)

     except InputGuardrailTripwireTriggered as e:
           print("Guardrail 2 block this input:" , e)

    # Example 3: Math question
     try:
        result = await Runner.run(triage_agent , "My homework: Solve 2x + 5 = 15")
        print(result.final_output)
        print(result.last_agent.name)

     except InputGuardrailTripwireTriggered as e:
          print("Guardrail 3 block this input:", e)
if __name__ == "__main__":
    asyncio.run(main())



