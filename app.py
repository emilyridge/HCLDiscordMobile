import tkinter as tk
from tkinter import messagebox
from models import Message


def display_message():
    messagebox.showinfo("Message", "Hello this is a local application")


app = tk.Tk()
app.title("Local Application")


messageTemplate = Message(author="Bob", recipient="Alice", timestamp="2024-03-01T12:12:12", message="Hello Alice, this is Bob.")
print(messageTemplate)

app.mainloop()