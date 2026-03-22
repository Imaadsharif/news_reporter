from src.agents import research_agent, summarizer_agent, writer_agent
from src.validators import validate_research, validate_summary, validate_writer

def run_pipeline(topic):
    # 🔍 Research
    research = research_agent(topic)

    if not validate_research(research):
        raise ValueError("Research validation failed")

    # 📌 Summary
    summary = summarizer_agent(research)

    if not validate_summary(summary):
        raise ValueError("Summary validation failed")

    # 📰 Final
    final = writer_agent(summary)

    if not validate_writer(final):
        raise ValueError("Final output validation failed")

    return {
        "research": research,
        "summary": summary,
        "final": final
    }