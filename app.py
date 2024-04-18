import tkinter as tk
from tkinter import messagebox, font, ttk
from tkinter import messagebox
from models import Message

WIDTH_IPHONE_15_MAX = 1290
HEIGHT_IPHONE_15_MAX = 2796

# @@ -7,35 +8,100 @@ HEIGHT_IPHONE_15_MAX = 2796
WIDTH_SCREEN = int(WIDTH_IPHONE_15_MAX/4)
HEIGHT_SCREEN = int(HEIGHT_IPHONE_15_MAX/4)

# Chat screen related functions
def init_function():
    # Add any initialization code here
    createChannelFrame()
    createChatFrame()
    createMessageFrame()

def createChannelFrame():
    channelFrame = tk.Frame(app, highlightthickness=3, highlightbackground="black")
    channelFrame.grid(row=0, column=0)

  # After some testing, a width of 17 allows the label to span the screen without making the window too much bigger
    channelName = tk.Label(channelFrame, text= "# Channel", font=("Arial", 25), width=17, foreground="White", background="#31343b")
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
    chat_display = tk.Text(chatFrame, bg="#31343b", fg="white", wrap=tk.WORD, width=17*2+6, highlightthickness=0, height=38)
    chat_display.grid(row=0, column=0)
    chat_display.tag_configure("user_message", foreground="white")


def on_entry_click(event):
    global entry_has_focus
    entry_has_focus = True
    if entry.get() == "Message #Channel":
        entry.delete(0, tk.END)
        entry.config(foreground="white")

def on_focus_out(event):
    global entry_has_focus
    entry_has_focus = False
    if not entry.get():
        entry.insert(0, "Message #Channel")
        entry.config(foreground="gray")

def createMessageFrame():
    global entry
    global entry_has_focus

    # This is where the user will type their message before sending.
    messageFrame = tk.Frame(app)
    messageFrame.configure(background="#31343b")
    messageFrame.grid(row=2, column=0)


    # Entry widget for user input with a specific font
    entry_font = font.Font(family="Helvetica", size=12)
    entry = tk.Entry(messageFrame, bg="#202427", fg="gray", font=entry_font)
    entry_has_focus = False


    entry.insert(0, "Message #Channel")
    entry.grid(row=0, column=2, padx=5, pady=5)


     # Bind events to the entry widget
    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_focus_out)
        
    # Button to send messages
    send_button = tk.Button(messageFrame, text="Send", command=send_message)
    send_button.grid(row=0, column=3, padx=5, pady=5)

    # Button that toggles reply mode
    reply_button = tk.Button(messageFrame, text="Reply", command=reply_mode_toggle)
    reply_button.grid(row=0, column=0, padx=5, pady=5)

    # Button to attach files
    file_button = tk.Button(messageFrame, text="File+", command=attach_file)
    file_button.grid(row=0, column=1, padx=5, pady=5)
<<<<<<< HEAD

=======
>>>>>>> 279f174 ([SCRN-2] Created the minimal channel screen.)


def send_message():
    message = entry.get()
    if message:
        # Insert the message into the chat display
        chat_display.insert(tk.END, f"User: {message}\n", "user_message")
        
        # Clear the entry widget after sending the message
        entry.delete(0, tk.END)

def check_enter_input(event):
    global entry_has_focus

    # If the entry box is in focus, attempt to send a message
    if entry_has_focus:
        send_message()

def reply_mode_toggle():
    pass
<<<<<<< HEAD
=======

def attach_file():
    pass
>>>>>>> 279f174 ([SCRN-2] Created the minimal channel screen.)

def attach_file():
    pass

# Channel information related functions
def init_channel_screen():
    channel_screen_name()
    channel_screen_users()

def channel_screen_name():
    channel_info_frame = tk.Frame(app, highlightthickness=3, highlightbackground="black", background="#31343b")
    channel_info_frame.grid(row=0, column=0)

    # After some testing, a width of 17 allows the label to span the screen without making the window too much bigger
    channelName = tk.Label(channel_info_frame, text= "# Channel", font=("Arial", 25), width=17, foreground="White", background="#31343b")
    channelName.grid(row=0, column=0, columnspan=3, pady=10)

    pins_button = tk.Button(channel_info_frame, text="Pins", command=pins_button_pressed)
    pins_button.grid(row=1, column=0)
    pins_label = tk.Label(channel_info_frame, text= "Pins", foreground="White", background="#31343b")
    pins_label.grid(row=2, column=0)

    threads_button = tk.Button(channel_info_frame, text="Threads", command=threads_button_pressed)
    threads_button.grid(row=1, column=1)
    threads_label = tk.Label(channel_info_frame, text= "Threads", foreground="White", background="#31343b")
    threads_label.grid(row=2, column=1)

    notifs_button = tk.Button(channel_info_frame, text="Notifs", command=notifs_button_pressed)
    notifs_button.grid(row=1, column=2)
    notifs_label = tk.Label(channel_info_frame, text= "Notifs", foreground="White", background="#31343b")
    notifs_label.grid(row=2, column=2, pady=10)

def channel_screen_users():
    user_frame = tk.Frame(app, background="#31343b")

def pins_button_pressed():
    pass

def threads_button_pressed():
    pass

def notifs_button_pressed():
    pass

# --------------------------------------

app = tk.Tk()
app.title("Discord Mobile Demo")

app.minsize(width=WIDTH_SCREEN, height=HEIGHT_SCREEN)

app.configure(background="#31343b")

#init_function()
init_channel_screen()

# Checks to see if the user presses the enter key.
app.bind("<Return>", check_enter_input)

app.mainloop()

