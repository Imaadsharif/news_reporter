def validate_research(text):
    if not text or len(text.strip()) < 50:
        return False
    return True