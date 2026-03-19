import os
import webbrowser

APPS = {
    "chrome": "start chrome",
    "vscode": "code",
    "postman": "start postman",
    "mongodb": "start mongod",
    "openvpn": "start openvpn",
    "whatsapp": "start whatsapp"
}

URLS = {
    "gmail": "https://mail.google.com",
    "whatsapp_web": "https://web.whatsapp.com"
}


def open_app(text):
    text = text.lower()

    for key, command in APPS.items():
        if key in text:
            os.system(command)
            return f"Opening {key}"

    return "App not found"


def open_url(text):
    text = text.lower()

    if "mail" in text or "gmail" in text:
        webbrowser.open(URLS["gmail"])
        return "Opening Gmail"

    if "whatsapp web" in text:
        webbrowser.open(URLS["whatsapp_web"])
        return "Opening WhatsApp Web"

    return None


def open_custom_link(text):
    if "http" in text:
        for word in text.split():
            if word.startswith("http"):
                webbrowser.open(word)
                return f"Opening {word}"

    return None