from langchain.agents import create_agent
import prompts
import config

def agent_creation(retriever_tool):
    agent = create_agent(
        model=config.AGENT_MODEL,
        tools=[retriever_tool],
        system_prompt=prompts.system_prompt,
    )
    return agent