import json
from datetime import datetime
import time


class Message:
    def __init__(self, author, recipient, timestamp, message):
        self.author = author
        self.recipient = recipient
        self.timestamp = timestamp # Format: YYYY-MM-DDTHH:MM:SS
        self.message = message

    def __str__(self):
        return f"From: {self.author}\n To: {self.recipient}\n Timestamp: {self.timestamp}\n Message: {self.message}\n"
    



    # Read in dummy data
    def read_in_dummy_data(json_file):
        with open(json_file, 'r') as file:
            messages_data = json.load(file)
        messages = []

        # Convert data into variables
        for data in messages_data:
            timestamp = datetime.strptime(data['timestamp'], '%Y-%m-%dT%H:%M:%S')
            message = Message(data['author'], data['recipient'], timestamp, data['message'])
            # add to array of messages
            messages.append(message)
        return messages
    

    def print_messages(messages):
        for message in messages:
            print(message)
    


    # This is an infinite loop for message scrolling effect
    # Don't call unless for display
    def scroll_messages(messages):
        index = 0
        while True:
            message = messages[index]
            print(message)
            
            # increase index if at end loop back to beginning
            index = (index + 1) % len(messages)