from core.assistant import handle_input
from utils.speaker import speak


def run():
    speak("Assistant started. How can I help you?")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            speak("Goodbye!")
            break

        handle_input(user_input)


if __name__ == "__main__":
    run()