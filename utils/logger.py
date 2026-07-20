from pathlib import Path
from datetime import datetime

LOG_FILE = Path("log.txt")
now = datetime.now()

def log(text):
    """
    Write logs to log.txt with timestamp.
    """

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(
            f"\n{'=' * 100}\n"
            f"Date: {now:%Y-%m-%d}\n"
            f"Time: {now:%H:%M:%S}\n"
            f"{text}\n"
        )
