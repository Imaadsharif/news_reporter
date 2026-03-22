def validate_summary(summary):
    if not summary or len(summary.strip()) < 20:
        return False

    if "-" not in summary and "•" not in summary:
        return False

    return True