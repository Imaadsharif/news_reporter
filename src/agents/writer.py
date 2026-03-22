from src.llm import call_llm

def writer_agent(summary):
    system = "Write a structured news article from the summary."
    return call_llm(system, summary)