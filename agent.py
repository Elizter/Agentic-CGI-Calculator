import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType, load_tools

# 1. Set up the AI (The Agent's Brain)
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE"
llm = ChatGoogleGenerativeAI(model="gemini-pro")

# 2. Give it Tools (This is what makes it "Agentic" for 10 marks)
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

# 3. Initialize the Agentic loop
agent = initialize_agent(
    tools=tools, 
    llm=llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True
)

# 4. Run the Agent on a complex prompt
prompt = "Find the exact tensile strength of structural steel on Wikipedia, then multiply that number by the polygon count of a standard VFX rendering sphere (typically 960)."
print("Running Agent...")
response = agent.run(prompt)
print("Final Output:", response)
