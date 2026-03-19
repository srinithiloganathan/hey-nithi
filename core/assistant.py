from core.intent_handler import detect_intent, extract_title
from utils.time_parser import extract_datetime
from utils.speaker import speak
from actions.scheduler import save_event, schedule_notification
from actions.app_launcher import open_app, open_url, open_custom_link


def handle_input(user_input):
    intent = detect_intent(user_input)

    if intent == "schedule_event":
        title = extract_title(user_input)
        dt = extract_datetime(user_input)

        if not dt:
            speak("I couldn't understand the time.")
            return

        event = save_event(title, dt)
        schedule_notification(title, dt, speak)

        speak(f"{title} scheduled on {event['time']}")

    elif intent == "open_app":
        result = open_custom_link(user_input)

        if not result:
            result = open_url(user_input)

        if not result:
            result = open_app(user_input)

        speak(result)

    else:
        speak("I don't understand that yet.")