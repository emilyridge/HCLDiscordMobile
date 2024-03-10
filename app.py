import tkinter as tk
from tkinter import messagebox, font

WIDTH_IPHONE_15_MAX = 1290
HEIGHT_IPHONE_15_MAX = 2796

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


def createChatFrame():
    global chat_display
    # This is where all the chat messages will be displayed.
    chatFrame = tk.Frame(app, highlightthickness=3, highlightbackground="gray")
    chatFrame.grid(row=1, column=0)

    # Create a label with the default font and text to measure its average width
    default_font = font.nametofont("TkDefaultFont")
    average_char_width = tk.Label(chatFrame, text="a", font=default_font).winfo_reqwidth()

    chat_display_width = int(WIDTH_SCREEN / average_char_width)

    # Chat display area (Text widget)
    chat_display = tk.Text(chatFrame, bg="black", fg="white", wrap=tk.WORD, width=chat_display_width)
    chat_display.grid(row=0, column=0, columnspan=2)
    chat_display.tag_configure("user_message", foreground="white")


def createMessageFrame():
    global entry
    # This is where the user will type their message before sending.
    messageFrame = tk.Frame(app)
    messageFrame.grid(row=2, column=0)

    tk.Label(messageFrame, text="Type your message here!").grid(row=0, column=0)

    # Entry widget for user input with a specific font
    entry_font = font.Font(family="Helvetica", size=12)
    entry = tk.Entry(messageFrame, bg="black", fg="white", font=entry_font)
    entry.grid(row=1, column=0)
        
    # Button to send messages
    send_button = tk.Button(messageFrame, text="Send", command=send_message)
    send_button.grid(row=1, column=1)


def send_message():
    message = entry.get()
    if message:
        # Insert the message into the chat display
        chat_display.insert(tk.END, f"User: {message}\n", "user_message")
        
        # Clear the entry widget after sending the message
        entry.delete(0, tk.END)


def display_message():
    messagebox.showinfo("Message", "Hello this is a local application")

app = tk.Tk()
app.title("Discord Mobile Demo")

app.minsize(width=WIDTH_SCREEN, height=HEIGHT_SCREEN)

init_function()

app.mainloop()