# Agentic-CGI-Calculator

This is an Agentic AI built with LangChain that uses external tools (Wikipedia and Math Evaluator) to solve complex mechanical/VFX queries. 

## How to Run (Evaluator Instructions)
1. Install dependencies: `pip install -r requirements.txt`
2. Insert your Google Gemini API key into line 7 of `agent.py`.
3. Run the script: `python agent.py`

## Example Terminal Output
```text
> Entering new AgentExecutor chain...
I need to find the tensile strength of structural steel and multiply it by 960.
Action: wikipedia
Action Input: Tensile strength of structural steel
Observation: Structural steel has a standard ultimate tensile strength of 400–550 MPa.
Thought: I will use 400 MPa for the calculation. 
Action: Calculator
Action Input: 400 * 960
Observation: 384000
Thought: I now know the final answer.
Final Answer: The calculated result for a standard VFX rendering sphere based on structural steel's base tensile strength is 384,000.

> Finished chain.
