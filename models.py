

class Message:
    def __init__(self, author, recipient, timestamp, message):
        self.author = author
        self.recipient = recipient
        self.timestap = timestamp # Format: YYYY-MM-DDTHH:MM:SS
        self.message = message

    def __str__(self):
        return f"From: {self.author}\n To: {self.recipient}\n Timestamp: {self.timestap}\n Message: {self.message}\n"