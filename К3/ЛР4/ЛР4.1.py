from datetime import datetime

class ActionLogger:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        with open("actions.log", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} — START: {self.name}\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open("actions.log", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now()} — END: {self.name}\n")
