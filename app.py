import tkinter as tk
from tkinter import messagebox

WIDTH_IPHONE_15_MAX = 1290
HEIGHT_IPHONE_15_MAX = 2796

WIDTH_SCREEN = int(WIDTH_IPHONE_15_MAX/4)
HEIGHT_SCREEN = int(HEIGHT_IPHONE_15_MAX/4)

def display_message():
    messagebox.showinfo("Message", "Hello this is a local application")


app = tk.Tk()
app.title("Local Application")


app.minsize(width=WIDTH_SCREEN, height=HEIGHT_SCREEN)

chatFrame = tk.Frame(app)
chatFrame.grid(row=0, column=0)

testLabel = tk.Label(chatFrame, text= "Hello world!")
testLabel.grid(row=0, column=0)

app.mainloop()