import tkinter as tk
from tkinter import messagebox

WIDTH_IPHONE_15_MAX = 1290
HEIGHT_IPHONE_15_MAX = 2796

WIDTH_SCREEN = int(WIDTH_IPHONE_15_MAX/4)
HEIGHT_SCREEN = int(HEIGHT_IPHONE_15_MAX/4)

def display_message():
    messagebox.showinfo("Message", "Hello this is a local application")


app = tk.Tk()
app.title("Discord Mobile Demo")


app.minsize(width=WIDTH_SCREEN, height=HEIGHT_SCREEN)

channelFrame = tk.Frame(app, highlightthickness=3, highlightbackground="black")
channelFrame.grid(row=0, column=0)

# After some testing, a width of 17 allows the label to span the screen without making the window too much bigger
channelName = tk.Label(channelFrame, text= "# Channel", font=("Arial", 25), width=17)
channelName.grid(row=0, column=1)

# This is where all the chat messages will be displayed.
chatFrame = tk.Frame(app, highlightthickness=3, highlightbackground="gray")
chatFrame.grid(row=1, column=0)

testLabel = tk.Label(chatFrame, text= "Hello world!", width=46, height=39)
testLabel.grid(row=0, column=0)

# This is where the user will type their message before sending.
messageFrame = tk.Frame(app)
messageFrame.grid(row=2, column=0)

tk.Label(messageFrame, text="Type your message here!").grid(row=0, column=0)


app.mainloop()