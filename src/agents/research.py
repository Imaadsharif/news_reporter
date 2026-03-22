from src.llm import call_llm

def research_agent(topic):
    system = "You are a research agent. Provide detailed factual information."
    return call_llm(system, topic)