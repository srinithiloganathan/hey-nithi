from datetime import datetime
from dateparser.search import search_dates


def extract_datetime(text):
    results = search_dates(
        text,
        settings={
            "PREFER_DATES_FROM": "future",
            "RELATIVE_BASE": datetime.now()
        }
    )

    if not results:
        return None

    return results[0][1]