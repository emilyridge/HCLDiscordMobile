import tkinter as tk
from tkinter import messagebox, font, ttk
from tkinter import messagebox
from models import Message

WIDTH_IPHONE_15_MAX = 1290
HEIGHT_IPHONE_15_MAX = 2796

# @@ -7,35 +8,100 @@ HEIGHT_IPHONE_15_MAX = 2796
WIDTH_SCREEN = int(WIDTH_IPHONE_15_MAX/4)
HEIGHT_SCREEN = int(HEIGHT_IPHONE_15_MAX/4)


def init_function():
    # Add any initialization code here
    createChannelFrame()
    createChatFrame()
    createMessageFrame()

def createChannelFrame():
    channelFrame = tk.Frame(app, highlightthickness=3, highlightbackground="black")
    channelFrame.grid(row=0, column=0)

  # After some testing, a width of 17 allows the label to span the screen without making the window too much bigger
    channelName = tk.Label(channelFrame, text= "# Channel", font=("Arial", 25), width=17)
    channelName.grid(row=0, column=1)




def on_entry_click(event):
    if entry.get() == "Message #Channel":
        entry.delete(0, tk.END)
        entry.config(foreground="white")

def on_focus_out(event):
    if not entry.get():
        entry.insert(0, "Message #Channel")
        entry.config(foreground="gray")

def createMessageFrame():
    global entry
    # This is where the user will type their message before sending.
    messageFrame = tk.Frame(app)
    messageFrame.configure(background="#31343b")
    messageFrame.grid(row=2, column=0)


    # Entry widget for user input with a specific font
    entry_font = font.Font(family="Helvetica", size=12)
    entry = tk.Entry(messageFrame, bg="#202427", fg="gray", font=entry_font)


    entry.insert(0, "Message #Channel")
    entry.grid(row=0, column=0)


     # Bind events to the entry widget
    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_focus_out)
        
    # Button to send messages
    send_button = tk.Button(messageFrame, text="Send", command=send_message)
    send_button.grid(row=0, column=1)


def send_message():
    message = entry.get()
    if message:
        # Insert the message into the chat display
        chat_display.insert(tk.END, f"User: {message}\n", "user_message")
        
        # Clear the entry widget after sending the message
        entry.delete(0, tk.END)


WIDTH_IPHONE_15_MAX = 1290
HEIGHT_IPHONE_15_MAX = 2796

WIDTH_SCREEN = int(WIDTH_IPHONE_15_MAX/4)
HEIGHT_SCREEN = int(HEIGHT_IPHONE_15_MAX/4)

def display_message():
    messagebox.showinfo("Message", "Hello this is a local application")

app = tk.Tk()
app.title("Discord Mobile Demo")

app.minsize(width=WIDTH_SCREEN, height=HEIGHT_SCREEN)

app.configure(background="#31343b")

init_function()

app.mainloop()