def validate_writer(output):
    if not output or len(output.strip()) < 100:
        return False
    return True