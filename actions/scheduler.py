import json
import os
import threading
import time
from datetime import datetime
from plyer import notification

FILE = "data/events.json"


def save_event(title, dt):
    event = {
        "title": title,
        "time": dt.strftime("%Y-%m-%d %H:%M:%S")
    }

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(event)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

    return event


def schedule_notification(title, event_time, speak_fn):
    def notify():
        while True:
            if datetime.now() >= event_time:
                notification.notify(
                    title="Reminder 🔔",
                    message=f"{title} is now!",
                    timeout=10
                )
                speak_fn(f"{title} is happening now")
                break

            time.sleep(2)

    threading.Thread(target=notify, daemon=True).start()