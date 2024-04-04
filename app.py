from tkinter import messagebox, font, ttk
import tkinter as tk
from tkinter import messagebox

def display_message():
    messagebox.showinfo("Message", "Hello this is a local application")

app = tk.Tk()
app.title("Local Application")

app.mainloop()