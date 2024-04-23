import tkinter as tk
from tkinter import messagebox, font, ttk
from models import Message
import os
import datetime
from uiobjects import *

WIDTH_IPHONE_15_MAX = 1290
HEIGHT_IPHONE_15_MAX = 2796

# @@ -7,35 +8,100 @@ HEIGHT_IPHONE_15_MAX = 2796
WIDTH_SCREEN = int(WIDTH_IPHONE_15_MAX/4)
HEIGHT_SCREEN = int(HEIGHT_IPHONE_15_MAX/4)
ROOT = os.getcwd()

message_list = []

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
    global chatFrame
    global empty_message_buffer

    # This is where all the chat messages will be displayed.
    chatFrame = ScrollableFrame(app, width=WIDTH_SCREEN, height=HEIGHT_SCREEN-110)
    chatFrame.grid_propagate(0)
    chatFrame.grid(row=1, column=0)

    # Create a label with the default font and text to measure its average width
    default_font = font.nametofont("TkDefaultFont")
    average_char_width = tk.Label(chatFrame.interior, text="a", font=default_font).winfo_reqwidth()

    chat_display_width = int(WIDTH_SCREEN / average_char_width)

    # Chat display area (Text widget)
    #chat_display = tk.Text(chatFrame, bg="#31343b", fg="white", wrap=tk.WORD, width=17*2+6, highlightthickness=0, height=38)
    #chat_display.grid(row=0, column=0)
    #chat_display.tag_configure("user_message", foreground="white")

    really_long_test_message = ("This is a test with a really long message, like way too long." 
                        + " Imagine this is a super long rant that i'm going on, expressing a deep and possibly slightly controversial thought. Many may not agree, but I do not care as this message is very important to me and, maybe, me alone." 
                        + " But I expect that you will read it in full and reply in kind, otherwise I may get upset with your minimal or lack of response.")

    
    message_list.append(UserMessage(user=User("templates/Test_PF1.png", "GoofyGoober", "ONLINE"), timestamp="2024-03-10T11:35:00", message="This is a test.", master=chatFrame.interior))
    message_list.append(UserMessage(user=User("templates/Test_PF1.png", "GoofyGuber", "ONLINE"), timestamp="2024-03-10T11:38:00", message=really_long_test_message, master=chatFrame.interior))

    empty_message_size = 595

    for idx in range(len(message_list)):
        message_list[idx].grid(row=idx+1, column=0)
        empty_message_size -= message_list[idx].winfo_reqheight()
    
    empty_message_buffer = EmptyMessage(master=chatFrame.interior, height=empty_message_size)
    empty_message_buffer.grid(row=0, column=0, sticky='sw')
    

    
    


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
    global send_button

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
    entry.bind("<KeyRelease>", update_send_button_visibility)
        
    # Button to send messages
    send_button = tk.Button(messageFrame, text="Send", command=send_message)
    send_button.grid(row=0, column=3, padx=5, pady=5)
    #update_send_button_visibility()

    # Button that toggles reply mode
    reply_button = tk.Button(messageFrame, text="Reply", command=reply_mode_toggle)
    reply_button.grid(row=0, column=0, padx=5, pady=5)

    # Button to attach files
    file_button = tk.Button(messageFrame, text="File+", command=attach_file)
    file_button.grid(row=0, column=1, padx=5, pady=5)

    update_send_button_visibility()

def send_message():
    message = entry.get()
    if message:
        time = datetime.datetime.now()
        # Insert the message into the chat display
        new_chat_message = UserMessage(user=User("templates/Test_PF1.png", "User", "ONLINE"), timestamp=f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}", message=message, master=chatFrame.interior)
        message_list.append(new_chat_message)
        new_chat_message.grid(row=len(message_list), column=0)
        empty_message_buffer.configure(height=empty_message_buffer.winfo_reqheight() - new_chat_message.winfo_reqheight())
        
        # Clear the entry widget after sending the message
        entry.delete(0, tk.END)

def check_enter_input(event):
    global entry_has_focus

    # If the entry box is in focus, attempt to send a message
    if entry_has_focus:
        send_message()

def reply_mode_toggle():
    pass

def attach_file():
    pass

def attach_file():
    pass

def update_send_button_visibility(*args):
    default_message = "Message #Channel"
    if entry.get() and entry.get() != default_message:
        send_button.grid(row=0, column=3, padx=5, pady=5)
    else:
        send_button.grid_remove()


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

    # Pins button and label beneath it
    pins_button = tk.Button(channel_info_frame, text="Pins", command=pins_button_pressed)
    pins_button.grid(row=1, column=0)
    pins_label = tk.Label(channel_info_frame, text= "Pins", foreground="White", background="#31343b")
    pins_label.grid(row=2, column=0)

    # Threads button and label beneath it
    threads_button = tk.Button(channel_info_frame, text="Threads", command=threads_button_pressed)
    threads_button.grid(row=1, column=1)
    threads_label = tk.Label(channel_info_frame, text= "Threads", foreground="White", background="#31343b")
    threads_label.grid(row=2, column=1)

    # Notification button and label beneath it
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

# Server list related functions
def init_server_screen():
    server_list()
    friends_list()
    server_channel_list()
    user_information()

def server_list():
    server_list_frame = tk.Frame(app, highlightthickness=3, highlightbackground="black", background="#31343b", height=HEIGHT_SCREEN-75, width=int(WIDTH_SCREEN/3)-40)
    server_list_frame.grid(row=0, column=0, sticky="n")
    server_list_frame.grid_propagate(0)

    # Add frame data structures that act like servers.
    test_img = tk.PhotoImage(file='templates/Test_PF1.png', width=35, height=35)
    
    # This is a bunch of test servers.
    tk.Label(server_list_frame, image=test_img).grid(row=0, column=0, pady=5, padx=12)
    tk.Label(server_list_frame, image=test_img).grid(row=1, column=0, pady=5, padx=12)
    tk.Label(server_list_frame, image=test_img).grid(row=2, column=0, pady=5, padx=12)
    tk.Label(server_list_frame, image=test_img).grid(row=3, column=0, pady=5, padx=12)
    tk.Label(server_list_frame, image=test_img).grid(row=4, column=0, pady=5, padx=12)
    tk.Label(server_list_frame, image=test_img).grid(row=5, column=0, pady=5, padx=12)
    tk.Label(server_list_frame, image=test_img).grid(row=6, column=0, pady=5, padx=12)
    tk.Label(server_list_frame, image=test_img).grid(row=7, column=0, pady=5, padx=12)
    tk.Label(server_list_frame, image=test_img).grid(row=8, column=0, pady=5, padx=12)
    tk.Label(server_list_frame, image=test_img).grid(row=9, column=0, pady=5, padx=12)
    tk.Label(server_list_frame, image=test_img).grid(row=10, column=0, pady=5, padx=12)
    tk.Label(server_list_frame, image=test_img).grid(row=11, column=0, pady=5, padx=12)


def friends_list():
    FRAME_SIZE = int(WIDTH_SCREEN/3)+20

    friends_list_frame = tk.Frame(app, highlightthickness=3, highlightbackground="black", background="#31343b", height=HEIGHT_SCREEN-75, width=FRAME_SIZE)
    friends_list_frame.grid(row=0, column=1, sticky="n")
    friends_list_frame.grid_propagate(0)

    # Friends button and label beside it
    friends_button = tk.Button(friends_list_frame, text="F")
    friends_button.grid(row=1, column=0, padx=10)
    friends_button_label = tk.Label(friends_list_frame, text="Friends", foreground="White", background="#31343b", font=("Arial", 15))
    friends_button_label.grid(row=1, column=1)

    # Nitro button and label beside it
    nitro_button = tk.Button(friends_list_frame, text="N")
    nitro_button.grid(row=2, column=0, padx=10)
    nitro_button_label = tk.Label(friends_list_frame, text="Nitro", foreground="White", background="#31343b", font=("Arial", 15))
    nitro_button_label.grid(row=2, column=1)

    # An entry to search through your friends list.
    entry_font = font.Font(family="Helvetica", size=12)
    friend_search_entry = tk.Entry(friends_list_frame, bg="#202427", fg="gray", font=entry_font, width=13)
    friend_search_entry.grid(row=3, column=0, columnspan=2)

    # DM button and label beside it. Would allow you to create a new dm group.
    dm_button = tk.Button(friends_list_frame, text="+")
    dm_button.grid(row=4, column=0)
    dm_button_label = tk.Label(friends_list_frame, text="Direct\nMessages", foreground="White", background="#31343b", font=("Arial", 13))
    dm_button_label.grid(row=4, column=1)

    # Add data structures that switch to dms.

def server_channel_list():
    channel_list_frame = tk.Frame(app, highlightthickness=3, highlightbackground="black", background="#31343b", height=HEIGHT_SCREEN, width=int(WIDTH_SCREEN/3)+20)
    channel_list_frame.grid(row=0, column=2, rowspan=2, sticky="n")
    channel_list_frame.grid_propagate(0)

    server_label = tk.Label(channel_list_frame, text="Server", foreground="White", background="#31343b", font=("Arial", 15))
    server_label.grid(row=0, column=0, sticky="n", columnspan=2)

    event_button = tk.Button(channel_list_frame, text="E")
    event_button.grid(row=1, column=0, padx=5)
    event_button_label = tk.Label(channel_list_frame, text="Events", foreground="White", background="#31343b", font=("Arial", 15))
    event_button_label.grid(row=1, column=1)

    # Add frame data structures that act as channels

def user_information():
    user_info_frame = tk.Frame(app, highlightthickness=3, highlightbackground="black", background="#31343b", height=75, width=int(WIDTH_SCREEN/3) + int(WIDTH_SCREEN/3) - 20)
    user_info_frame.grid(row=1, column=0, columnspan=2, sticky="n")
    # grid_propagate disables dynamic frame scaling, so the frames will always be the same size.
    user_info_frame.grid_propagate(0)

    # User information
    username_label = tk.Label(user_info_frame, text="Test Username", font=("Arial", 10), foreground="White", background="#31343b")
    username_label.grid(row=0, column=1, sticky="w")
    user_status_label = tk.Label(user_info_frame, text="Online", foreground="White", background="#31343b")
    user_status_label.grid(row=1, column=1, sticky="w")

    # Mute button
    mute_button = tk.Button(user_info_frame, text="M")
    mute_button.grid(row=0, column=2, rowspan=2)

    # Deafen button
    deafen_button = tk.Button(user_info_frame, text="D")
    deafen_button.grid(row=0, column=3, rowspan=2)

    # Profile picture
    test_img = tk.PhotoImage(file='templates/Test_PF1.png', width=35, height=35)
    pf_picture = tk.Label(user_info_frame, image=test_img)
    pf_picture.grid(row=0, column=0, rowspan=3, pady=15)

# --------------------------------------

app = tk.Tk()
app.title("Discord Mobile Demo")

app.minsize(width=WIDTH_SCREEN, height=HEIGHT_SCREEN)

app.configure(background="#31343b")

init_function()
#init_channel_screen()
#init_server_screen()

ttk.Style

# Checks to see if the user presses the enter key.
app.bind("<Return>", check_enter_input)

app.mainloop()

