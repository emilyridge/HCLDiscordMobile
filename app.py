import tkinter as tk
from tkinter import font, filedialog
from PIL import Image, ImageTk
import os
import datetime
from uiobjects import *

WIDTH_IPHONE_15_MAX = 1290
HEIGHT_IPHONE_15_MAX = 2796

WIDTH_SCREEN = 419
HEIGHT_SCREEN = int(HEIGHT_IPHONE_15_MAX/4)
ROOT = os.getcwd()

message_list = []

# Global variables for frames (different screens)
chatScreenFrame = None
channelScreenFrame = None
serverScreenFrame = None

# Reply frame stuff
reply_buffer = None
reply_pf = None
reply_username = None
reply_message = None

# Button images
## Chat buttons
send_button_img = None
file_add_img = None
reply_button_img = None

## Channel Buttons
pins_button_img = None
threads_button_img = None
notifs_button_img = None
mention_button_img = None

## Server Buttons
mute_button_img = None
depressed_mute_button_img = None
deafen_button_img = None
depressed_deafen_button_img = None
friends_button_img = None
nitro_button_img = None
new_dm_img = None
events_button_img = None



# Chat screen related functions
def init_function():
    global chatScreenFrame
    # Add any initialization code here
    chatScreenFrame = tk.Frame(app, background="#31343b")
    createChannelFrame()
    createChatFrame()
    createMessageFrame()

def createChannelFrame():
    global channelFrame
    channelFrame = tk.Frame(chatScreenFrame, highlightthickness=3, highlightbackground="black")
    channelFrame.grid(row=0, column=0)

    channelName = tk.Label(channelFrame, text= "# Channel", font=("Arial", 25), width=21, foreground="White", background="#31343b")
    channelName.grid(row=0, column=1)

def createChatFrame():
    global chatFrame
    global empty_message_buffer

    # This is where all the chat messages will be displayed.
    chatFrame = ScrollableFrame(chatScreenFrame, width=WIDTH_SCREEN, height=HEIGHT_SCREEN-110)
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

    message_list.append(UserMessage(user=User("templates/Test_PF2.png", "GoofyGoober", "ONLINE"), timestamp="2024-03-10T11:35:00", message="This is a test.", reply_function=reply_message_clicked, master=chatFrame.interior))
    message_list.append(UserMessage(user=User("templates/Test_PF3.png", "GoofyGuber", "ONLINE"), timestamp="2024-03-10T11:38:00", message=really_long_test_message, reply_function=reply_message_clicked, master=chatFrame.interior))

    empty_message_size = 595

    for idx in range(len(message_list)):
        message_list[idx].grid(row=idx+1, column=0)
        empty_message_size -= message_list[idx].winfo_reqheight()
    
    empty_message_buffer = EmptyMessage(master=chatFrame.interior, height=empty_message_size)
    empty_message_buffer.grid(row=0, column=0, sticky='sw')
    

# Check for when the entry box is clicked on
def on_entry_click(event):
    global entry_has_focus
    entry_has_focus = True
    if entry.get() == "Message #Channel":
        entry.delete(0, tk.END)
        entry.config(foreground="white")

# Check for when the entry box is clicked off of
def on_focus_out(event):
    global entry_has_focus
    entry_has_focus = False
    if not entry.get():
        entry.insert(0, "Message #Channel")
        entry.config(foreground="gray")

def createMessageFrame():
    global entry
    global entry_has_focus
    global messageFrame
    global label
    global send_button
    global reply_button
    global reply_frame

    # This is where the user will type their message before sending.
    messageFrame = tk.Frame(chatScreenFrame)
    messageFrame.configure(background="#31343b")
    messageFrame.grid(row=3, column=0)

    # Preview for reply message
    reply_frame = tk.Frame(chatScreenFrame, bg="#31343b", width=WIDTH_SCREEN)
    reply_frame.grid(row=2, column=0, sticky='w')


    # Entry widget for user input with a specific font
    entry_font = font.Font(family="Helvetica", size=12)
    entry = tk.Entry(messageFrame, bg="#202427", fg="gray", font=entry_font, width=25)
    entry_has_focus = False

    # Add temporary text prompt in the entry box
    entry.insert(0, "Message #Channel")
    entry.grid(row=1, column=2, padx=5, pady=5)


     # Bind events to the entry widget
    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_focus_out)
    entry.bind("<KeyRelease>", update_send_button_visibility)
        
    # Button to send messages
    send_button = tk.Button(messageFrame, image=send_button_img, command=send_message, activebackground="#31343b", background="#31343b")
    label = tk.Label(messageFrame, text="", background="#31343b", width=5)

    label.grid(row=0, column=3, padx=5, pady=5)
    send_button.grid(row=1, column=3, padx=5, pady=5)
     

    # Button that toggles reply mode
    reply_button = tk.Button(messageFrame, image=reply_button_img, command=reply_mode_toggle, activebackground="#31343b", background="#31343b")
    reply_button.grid(row=1, column=0, padx=5, pady=5)
    reply_button.pressed = False
    reply_button.message = None

    # Button to attach files
    file_button = tk.Button(messageFrame, image=file_add_img, command=attach_file, activebackground="#31343b", background="#31343b")
    file_button.grid(row=1, column=1, padx=5, pady=5)

    # Update the send button's visiblity
    update_send_button_visibility()

def send_message():
    message = entry.get()
    if message and entry_has_focus:
        time = datetime.datetime.now()
        # Insert the message into the chat display
        new_chat_message = UserMessage(user=User("templates/Test_PF1.png", "User", "ONLINE"), timestamp=f"{time.year}-{time.month}-{time.day}T{time.hour}:{time.minute}:{time.second}", 
                                       message=message, reply_function=reply_message_clicked, reply_message=reply_button.message, master=chatFrame.interior)
        message_list.append(new_chat_message)
        new_chat_message.grid(row=len(message_list), column=0)
        empty_message_buffer.configure(height=empty_message_buffer.winfo_reqheight() - new_chat_message.winfo_reqheight())

        # If the reply button is toggled on, 
        # then ensure that this button can be replied to
        new_chat_message.reply_button_pressed(reply_button.pressed)
        
        # Clear the entry widget after sending the message
        entry.delete(0, tk.END)

        # In case the user uses the send button, this will update the send button
        update_send_button_visibility()

        # Toggle reply mode if the button is pressed and the user replied to a message.
        if reply_button.pressed and reply_button.message:
            reply_mode_toggle()

def check_enter_input(event):
    # If the entry box is in focus, attempt to send a message
    if entry_has_focus:
        send_message()

# This function is called when the reply button is clicked
def reply_mode_toggle():
    reply_button.pressed = not reply_button.pressed

    if reply_button.pressed:
        reply_button.configure(relief='sunken')
    
    else:
        reply_button.configure(relief='raised')
        reply_button.message = None
        reply_preview_clear()


    for message in message_list:
        message.reply_button_pressed(reply_button.pressed)

def reply_preview_clear():
    if not reply_pf is None:
        reply_pf.grid_forget()
        reply_username.grid_forget()
        reply_message.grid_forget()
        reply_buffer.grid_forget()
        reply_frame.configure(highlightthickness=0)
        chatFrame.configure_height(height=HEIGHT_SCREEN-110)

# This is called when in reply mode and when a message is clicked
def reply_message_clicked(message):
    global reply_pf
    global reply_pf_file
    global reply_username
    global reply_buffer
    global reply_message

    reply_button.message = message

    # Clear the current reply preview, if applicable
    reply_preview_clear()

    # Add room for the reply frame
    chatFrame.configure_height(height=HEIGHT_SCREEN-135)

    # This buffer helps center the reply message
    reply_buffer = tk.Label(reply_frame, width=3, bg="#31343b")
    reply_buffer.grid(row=0, column=0)

    # Add reply user's profile picture
    reply_pf_file = message.user.get_profile_picture(20)
    reply_pf = tk.Label(reply_frame, bg="#31343b", anchor='w', image=reply_pf_file)
    reply_pf.grid(row=0, column=1)

    # Add reply user's username
    reply_username = tk.Label(reply_frame, bg="#31343b", fg="White", text=message.user.get_username(), anchor='w', justify='left', font=("Arial", 10))
    reply_username.grid(row=0, column=2)

    message_str = message.message

    # If the message is too long, shorten it and add an ellipse
    if len(message.user.get_username()) + len(message_str) > 55:
        message_str = message_str[0:55] + "..."

    # Add reply message
    reply_message = tk.Label(reply_frame, bg="#31343b", foreground="White", text=message_str, anchor='w', justify='left', font=("Arial", 8))
    reply_message.grid(row=0, column=3)

def attach_file():
    # As a proof of concept, ask to open file.
    # Close it immediately to avoid memory leak.
    temp = filedialog.askopenfile()
    if not temp is None:
        temp.close()

# This is called when the entry is edited.
def update_send_button_visibility(event=None):
    default_message = "Message #Channel"
    if entry.get() and entry.get() != default_message:
        label.grid_remove()
        send_button.grid(row=1, column=3, padx=5, pady=5)

    else:
        send_button.grid_remove()
        label.grid(row=1, column=3, padx=5, pady=5)



# Channel information related functions
def init_channel_screen():
    global channelScreenFrame
    channelScreenFrame = tk.Frame(app, background="#31343b")

    channel_screen_name()
    channel_screen_users()

def channel_screen_name():
    channel_info_frame = tk.Frame(channelScreenFrame, highlightthickness=3, highlightbackground="black", background="#31343b")
    channel_info_frame.grid(row=0, column=0)

    # After some testing, a width of 17 allows the label to span the screen without making the window too much bigger
    channelName = tk.Label(channel_info_frame, text= "# Channel", font=("Arial", 25), width=21, foreground="White", background="#31343b")
    channelName.grid(row=0, column=0, columnspan=3, pady=10)

    # Pins button and label beneath it
    pins_button = tk.Button(channel_info_frame, image=pins_button_img, command=pins_button_pressed, activebackground="#31343b", background="#31343b")
    pins_button.grid(row=1, column=0)
    pins_label = tk.Label(channel_info_frame, text= "Pins", foreground="White", background="#31343b")
    pins_label.grid(row=2, column=0)

    # Threads button and label beneath it
    threads_button = tk.Button(channel_info_frame, image=threads_button_img, command=threads_button_pressed, activebackground="#31343b", background="#31343b")
    threads_button.grid(row=1, column=1)
    threads_label = tk.Label(channel_info_frame, text= "Threads", foreground="White", background="#31343b")
    threads_label.grid(row=2, column=1)

    # Notification button and label beneath it
    notifs_button = tk.Button(channel_info_frame, image=notifs_button_img, command=notifs_button_pressed, activebackground="#31343b", background="#31343b")
    notifs_button.grid(row=1, column=2)
    notifs_label = tk.Label(channel_info_frame, text= "Notifs", foreground="White", background="#31343b")
    notifs_label.grid(row=2, column=2, pady=10)

def channel_screen_users():
    global user_frame
    user_frame = ScrollableFrame(channelScreenFrame, height=HEIGHT_SCREEN-100, width=WIDTH_SCREEN)
    user_frame.grid(row=1, column=0, sticky='e')

    # Add a RoleFrame
    role_frame1 = RoleFrame("Online", mention_button_pressed, master=user_frame.interior, width=53)
    role_frame1.grid(row=0, column=0, sticky='w')

    # Add users to the RoleFrame
    user1 = User("templates/Test_PF2.png", "GoofyGoober", "ONLINE")
    role_frame1.add_users(user1)
    user2 = User("templates/Test_PF3.png", "GoofyGuber", "ONLINE", "Playing Terraria")
    role_frame1.add_users(user2)

    # Add a second RoleFrame
    role_frame2 = RoleFrame("Admins", mention_button_pressed, role_color="Pink", master=user_frame.interior)
    role_frame2.grid(row=1, column=0, sticky='w')

    # Add a second group of users to the second RoleFrame
    testList = [User("templates/Test_PF4.png", "CyaMan", "OFFLINE"), User("templates/Test_PF5.png", "C@tLands", "OFFLINE"), User("templates/Test_PF6.png", "TestYall", "IDLE")]
    role_frame2.add_users(testList)

# These functions are here as placeholders,
# given more time these functions would be fleshed out.
def pins_button_pressed():
    pass

def threads_button_pressed():
    pass

def notifs_button_pressed():
    pass
# ---------------------------------------------------

def mention_button_pressed(user):

    if entry.get() == "Message #Channel":
        entry.delete(0, tk.END)
        entry.config(foreground="white")

    message = f" @{user}"

    # If the string is blank or there's a space at the end of the message,
    # then don't add a space at the beginning
    if not entry.get() or entry.get()[len(entry.get()) - 1] == " ":
        message = f"@{user}"

    entry.insert(len(entry.get()), message)
    update_send_button_visibility()
    switch_to_chat(None)

# Server list related functions
def init_server_screen():
    global serverScreenFrame
    serverScreenFrame = tk.Frame(app, background="#31343b")
    server_list()
    friends_list()
    server_channel_list()
    user_information()

def server_list():

    def get_server_picture(server_label : tk.Label, picture_str : str):
        if picture_str == "":
            picture_str = "templates/Test_PF1.png"


        server_label.picture = ImageTk.PhotoImage(Image.open(picture_str).resize((35, 35)))
        server_label.configure(image=server_label.picture)

    # Construct the server list frame
    server_list_frame = tk.Frame(serverScreenFrame, highlightthickness=3, highlightbackground="black", background="#31343b", height=HEIGHT_SCREEN-75, width=int(WIDTH_SCREEN/3)-40)
    server_list_frame.grid(row=0, column=0, sticky="n")
    server_list_scroll = ScrollableFrame(server_list_frame, height=HEIGHT_SCREEN-81, width=int(WIDTH_SCREEN/3)-40, background="#31343b")
    server_list_scroll.grid(row=0, column=0)
    server_list_scroll.grid_propagate(0)
    
    picture_list = ["templates/Server_Picture1.png", "templates/Server_Picture2.png", "templates/Test_PF5.png", "templates/Server_Picture3.png", "templates/Server_Picture4.png", "templates/Test_PF6.png", "templates/Server_Picture6.png", 
                    "templates/Test_PF4.png", "templates/Server_Picture7.png", "templates/Test_PF1.png", "templates/Server_Picture8.png", "templates/Server_Picture9.png", 
                    "templates/Server_Picture10.png", "templates/Test_PF3.png", "templates/Server_Picture11.png", "templates/Server_Picture12.png", "templates/Server_Picture13.png", "templates/Test_PF2.png"]

    # This is a bunch of test servers.
    for i in range(17):
        label = tk.Label(server_list_scroll.interior, background="#31343b")
        get_server_picture(label, picture_list[i])
        label.grid(row=i, column=0, pady=5, padx=12)



def friends_list():
    FRAME_SIZE = int(WIDTH_SCREEN/3)+20

    friends_list_frame = tk.Frame(serverScreenFrame, highlightthickness=3, highlightbackground="black", background="#31343b", height=HEIGHT_SCREEN-75, width=FRAME_SIZE)
    friends_list_frame.grid(row=0, column=1, sticky="n")
    

    # Friends button and label beside it
    friends_button = tk.Button(friends_list_frame, image=friends_button_img, activebackground="#31343b", background="#31343b")
    friends_button.grid(row=1, column=0, padx=10)
    friends_button_label = tk.Label(friends_list_frame, text="Friends", foreground="White", background="#31343b", font=("Arial", 15))
    friends_button_label.grid(row=1, column=1)

    # Nitro button and label beside it
    nitro_button = tk.Button(friends_list_frame, image=nitro_button_img, activebackground="#31343b", background="#31343b")
    nitro_button.grid(row=2, column=0, padx=10)
    nitro_button_label = tk.Label(friends_list_frame, text="Nitro", foreground="White", background="#31343b", font=("Arial", 15))
    nitro_button_label.grid(row=2, column=1)

    # An entry to search through your friends list.
    entry_font = font.Font(family="Helvetica", size=12)
    friend_search_entry = tk.Entry(friends_list_frame, bg="#202427", fg="gray", font=entry_font, width=13)
    friend_search_entry.grid(row=3, column=0, columnspan=2)

    # DM button and label beside it. Would allow you to create a new dm group.
    dm_button = tk.Button(friends_list_frame, image=new_dm_img, activebackground="#31343b", background="#31343b")
    dm_button.grid(row=4, column=0)
    dm_button_label = tk.Label(friends_list_frame, text="Direct\nMessages", foreground="White", background="#31343b", font=("Arial", 13))
    dm_button_label.grid(row=4, column=1)

    # Add data structures that switch to dms.
    friends_list_scroll = ScrollableFrame(friends_list_frame, background="#31343b", height=HEIGHT_SCREEN-229, width=FRAME_SIZE)
    friends_list_scroll.grid(row=5, column=0, columnspan=2, sticky="e")
    friends_list_scroll.grid_propagate(0)

    # Add users in friends list
    users = [User("templates/Test_PF2.png", "GoofyGoober", "ONLINE"), User("templates/Test_PF3.png", "GoofyGuber", "ONLINE", user_status_message="Playing Terraria"), User("templates/Test_PF4.png", "CyaMan", "ONLINE"),
             User("templates/Test_PF5.png", "C@tLands", "ONLINE"), User("templates/Test_PF6.png", "TestYall", "ONLINE"), User("templates/Server_Picture2.png", "Ramsay", "ONLINE", user_status_message="I'm not Gordon!"),
             User("templates/Server_Picture8.png", "WariosBike", "ONLINE"), User("templates/Server_Picture5.png", "SndwchDrvng", "ONLINE"), User("templates/Server_Picture13.png", "Spoons", "ONLINE"),
             User("templates/Server_Picture1.png", "MushrumManic", "ONLINE"), User("templates/Server_Picture6.png", "CoolKat29", "ONLINE"), User("templates/Server_Picture9.png", "UFrumFutur", "ONLINE", user_status_message="OUTATIME")]

    for i in range(len(users)):
        user1 = UserFrame(users[i], master=friends_list_scroll.interior, width=12)
        user1.grid(row=i, column=0)

def server_channel_list():
    # Initialize the server channel frame
    channel_list_frame = tk.Frame(serverScreenFrame, highlightthickness=3, highlightbackground="black", background="#31343b", height=HEIGHT_SCREEN, width=int(WIDTH_SCREEN/3)+20)
    channel_list_frame.grid(row=0, column=2, rowspan=2, sticky="n")
    

    server_label = tk.Label(channel_list_frame, text="Server", foreground="White", background="#31343b", font=("Arial", 15))
    server_label.grid(row=0, column=0, sticky="n", columnspan=2)

    event_button = tk.Button(channel_list_frame, image=events_button_img, activebackground="#31343b", background="#31343b")
    event_button.grid(row=1, column=0, padx=5)
    event_button_label = tk.Label(channel_list_frame, text="Events", foreground="White", background="#31343b", font=("Arial", 15))
    event_button_label.grid(row=1, column=1)

    channel_list_scroll = ScrollableFrame(channel_list_frame, height=HEIGHT_SCREEN-76, width=int(WIDTH_SCREEN/3))
    channel_list_scroll.grid(row=2, column=0, columnspan=3, sticky='e')
    channel_list_scroll.grid_propagate(0)

    # Adding a category and some channels.
    category_frame = ToggledFrame(channel_list_scroll.interior, text="Category 1")
    category_frame.grid(row=0, column=0, sticky='w')
    channel_frame1 = ChannelFrame(category_frame.sub_frame, text="Channel")
    category_frame.add_children([channel_frame1, ChannelFrame(category_frame.sub_frame, text="Channel2"), ChannelFrame(category_frame.sub_frame, text="Goober-Zone")])

    # Adding a thread to the Channel channel
    channel_frame1.add_children(ThreadFrame(channel_frame1.sub_frame, "Goober"))

    # Adding a VoiceChatFrame to the list.
    voice_chat1 = VoiceChatFrame(category_frame.sub_frame, "Voice Chat")
    category_frame.add_children(voice_chat1)

    # Adding a second category
    category_frame2 = ToggledFrame(channel_list_scroll.interior, text="General Chat")
    category_frame2.grid(row=1, column=0, sticky='w')
    category_frame2.add_children([ChannelFrame(category_frame2.sub_frame, text="Debates"), ChannelFrame(category_frame2.sub_frame, text="About-Cats"), ChannelFrame(category_frame2.sub_frame, text="general")])

    # Adding a third category
    category_frame3 = ToggledFrame(channel_list_scroll.interior, text="Voice Chats")
    category_frame3.grid(row=2, column=0, sticky='w')
    category_frame3.add_children([VoiceChatFrame(category_frame3.sub_frame, text="General VC"), VoiceChatFrame(category_frame3.sub_frame, text="Chaos Chat"), VoiceChatFrame(category_frame3.sub_frame, text="idle"),
                                  VoiceChatFrame(category_frame3.sub_frame, text="Midnight Watch"), VoiceChatFrame(category_frame3.sub_frame, text="Dogfighterz")])
    
    # Adding a fourth category
    category_frame4 = ToggledFrame(channel_list_scroll.interior, text="Beeg Category")
    category_frame4.grid(row=3, column=0, sticky='w')
    category_frame4.add_children([ChannelFrame(category_frame4.sub_frame, text="Funni-Dogs"), ChannelFrame(category_frame4.sub_frame, text="OCs"), ChannelFrame(category_frame4.sub_frame, text="Memes"),
                                  ChannelFrame(category_frame4.sub_frame, text="Frogs"), ChannelFrame(category_frame4.sub_frame, text="Castle-Designs"),
                                  ChannelFrame(category_frame4.sub_frame, text="Lousy-Devils"), ChannelFrame(category_frame4.sub_frame, text="Failure-Cars"),
                                  ChannelFrame(category_frame4.sub_frame, text="Desert-Bus"), ChannelFrame(category_frame4.sub_frame, text="MM2-Levels"),
                                  ChannelFrame(category_frame4.sub_frame, text="Jon Kirby"), ChannelFrame(category_frame4.sub_frame, text="Dont-Sue"),
                                  VoiceChatFrame(category_frame4.sub_frame, text="Chatterz"), VoiceChatFrame(category_frame4.sub_frame, text="Logs")])




def user_information():
    global mute_button
    global deafen_button

    user_info_frame = tk.Frame(serverScreenFrame, highlightthickness=3, highlightbackground="black", background="#31343b", height=75, width=286)
    user_info_frame.grid(row=1, column=0, columnspan=2, sticky="n")
    # grid_propagate disables dynamic frame scaling, so the frames will always be the same size.
    user_info_frame.grid_propagate(0)

    # User information
    username_label = tk.Label(user_info_frame, text="User", anchor='w', justify='left', font=("Arial", 10), foreground="White", background="#31343b", width=19)
    username_label.grid(row=0, column=1, sticky="w")
    user_status_label = tk.Label(user_info_frame, text="Online", foreground="White", background="#31343b")
    user_status_label.grid(row=1, column=1, sticky="w")

    # Mute button
    mute_button = tk.Button(user_info_frame, image=mute_button_img, activebackground="#31343b", background="#31343b", command=mute_button_pressed)
    mute_button.grid(row=0, column=2, rowspan=2)
    mute_button.pressed = False

    # Deafen button
    deafen_button = tk.Button(user_info_frame, image=deafen_button_img, activebackground="#31343b", background="#31343b", command=deafen_button_pressed)
    deafen_button.grid(row=0, column=3, rowspan=2)
    deafen_button.pressed = False

    # Profile picture
    pf_picture = tk.Label(user_info_frame, image=test_img, background="#31343b")
    pf_picture.grid(row=0, column=0, rowspan=3, pady=15)

# Changes the look of the mute button
def mute_button_pressed():
    
    if mute_button.pressed or deafen_button.pressed:
        mute_button.pressed = False
        mute_button.configure(image=mute_button_img)
        
        # If the mute button is pressed when the deafen button is already depressed,
        # then unmute and undeafen.
        if deafen_button.pressed:
            deafen_button_pressed()

    else:
        mute_button.pressed = True
        mute_button.configure(image=depressed_mute_button_img)

# Changes the look of the deafen button
def deafen_button_pressed():
    
    if deafen_button.pressed:
        deafen_button.pressed = False
        deafen_button.configure(image=deafen_button_img)

        # If the user wasn't muted before deafening, then unmute
        if not mute_button.pressed:
            mute_button.configure(image=mute_button_img)
    
    else:
        deafen_button.pressed = True
        deafen_button.configure(image=depressed_deafen_button_img)

        # When deafened, the user is also muted
        mute_button.configure(image=depressed_mute_button_img)


# Functions to change display (resembling swipe)
def switch_to_chat(event):
    channelScreenFrame.grid_forget()
    serverScreenFrame.grid_forget()
    chatScreenFrame.grid(row=0, column=0)

def switch_to_channel(event):
    chatScreenFrame.grid_forget()
    serverScreenFrame.grid_forget()
    channelScreenFrame.grid(row=0, column=0)

def switch_to_server(event):
    chatScreenFrame.grid_forget()
    channelScreenFrame.grid_forget()
    serverScreenFrame.grid(row=0, column=0)



def initialize_button_images():
    global send_button_img
    global file_add_img
    global reply_button_img

    send_button_img = ImageTk.PhotoImage(Image.open("templates/Buttons/Send_Button.png").resize((35, 35)))
    file_add_img = ImageTk.PhotoImage(Image.open("templates/Buttons/File_Add_Button.png").resize((35, 35)))
    reply_button_img = ImageTk.PhotoImage(Image.open("templates/Buttons/Reply_Button.png").resize((35, 35)))
 
    global pins_button_img
    global threads_button_img
    global notifs_button_img

    pins_button_img = ImageTk.PhotoImage(Image.open("templates/Buttons/Pins_Button.png").resize((35, 35)))
    threads_button_img = ImageTk.PhotoImage(Image.open("templates/Buttons/Threads_Button.png").resize((35, 35)))
    notifs_button_img = ImageTk.PhotoImage(Image.open("templates/Buttons/Notif_Button.png").resize((35, 35)))


    global mute_button_img
    global depressed_mute_button_img
    global deafen_button_img
    global depressed_deafen_button_img
    global friends_button_img
    global nitro_button_img
    global new_dm_img
    global events_button_img

    mute_button_img = ImageTk.PhotoImage(Image.open("templates/Buttons/Microphone_Button.png").resize((35, 35)))
    depressed_mute_button_img = ImageTk.PhotoImage(Image.open("templates/Buttons/Microphone_Button_Depressed.png").resize((35, 35)))
    deafen_button_img = ImageTk.PhotoImage(Image.open("templates/Buttons/Deafen_Button.png").resize((35, 35)))
    depressed_deafen_button_img = ImageTk.PhotoImage(Image.open("templates/Buttons/Deafen_Button_Depressed.png").resize((35, 35)))
    friends_button_img = ImageTk.PhotoImage(Image.open("templates/Buttons/Friends_Button.png").resize((35, 35)))
    nitro_button_img = ImageTk.PhotoImage(Image.open("templates/Buttons/Nitro_Button.png").resize((35, 35)))
    new_dm_img = ImageTk.PhotoImage(Image.open("templates/Buttons/New_DM_Button.png").resize((35, 35)))
    events_button_img = ImageTk.PhotoImage(Image.open("templates/Buttons/Events_Button.png").resize((35, 35)))

    


# --------------------------------------
# Initialize the app
app = tk.Tk()
app.title("Discord Mobile Demo")

# Set bounds for app
app.minsize(width=WIDTH_SCREEN, height=HEIGHT_SCREEN)
app.maxsize(width=WIDTH_SCREEN, height=HEIGHT_SCREEN)
app.configure(background="#31343b")

# Initalize the default profile picture
test_img = Image.open("templates/Test_PF1.png").resize((35,35))
test_img = ImageTk.PhotoImage(test_img)

# Initalize pictures and frames
initialize_button_images()
init_function()
init_channel_screen()
init_server_screen()
chatScreenFrame.grid(row=0, column=0)

# Bind functiond to function keys
app.bind("<F1>", switch_to_server)
app.bind("<F2>", switch_to_chat)
app.bind("<F3>", switch_to_channel)

# Checks to see if the user presses the enter key.
app.bind("<Return>", check_enter_input)

# Start app
app.mainloop()

