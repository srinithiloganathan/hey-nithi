def detect_intent(text):
    text = text.lower()

    if "schedule" in text or "meeting" in text or "call" in text:
        return "schedule_event"

    if "open" in text:
        return "open_app"

    return "unknown"


def extract_title(text):
    text = text.lower()

    if "meeting" in text:
        return "Meeting"
    elif "call" in text:
        return "Call"

    return "Event"