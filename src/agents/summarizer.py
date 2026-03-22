from src.llm import call_llm

def summarizer_agent(text):
    system = "Summarize the content into clear bullet points."
    return call_llm(system, text)