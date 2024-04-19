import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from typing import Literal

WIDTH_IPHONE_15_MAX = 1290
HEIGHT_IPHONE_15_MAX = 2796
WIDTH_SCREEN = int(WIDTH_IPHONE_15_MAX/4)
HEIGHT_SCREEN = int(HEIGHT_IPHONE_15_MAX/4)

class User:
    
    STATUS = {"ONLINE": 0, "IDLE": 1, "DND": 2, "OFFLINE": 3}
    STATUS_MESSAGE = {0: "ONLINE", 1: "IDLE", 2: "DND", 3: "OFFLINE"}

    user_pf = ""
    username = ""
    user_status = STATUS["OFFLINE"]

    def __init__(self, user_pf : str, username : str, user_status: Literal["ONLINE", "IDLE", "DND", "OFFLINE"]) -> None:
        """
        Parameters
        ----------
        user_pf : str
            A string that has the location of a user's profile picture.
        
        username: str
            The user's display username.

        user_status: str
            The user's current status. Valid values ONLINE, IDLE, DND, and OFFLINE.
        """

        if not isinstance(user_pf, str):
            raise TypeError(f"user_pf should be of type str, got {type(user_pf)} instead")
        if user_pf == "":
            raise ValueError("User's profile picture must have a value.")
        self.user_pf = user_pf
        

        if not isinstance(username, str):
            raise TypeError(f"Username should be of type str, got {type(username)} instead")
        if len(username) == 0:
            raise ValueError("Username must contain at least 1 character")
        self.username = username

        if not user_status in self.STATUS.keys():
            raise ValueError(f"User status can only be set to the values ONLINE, IDLE, DND, or OFFLINE, received {user_status} instead")
        self.user_status = self.STATUS[user_status] if user_status in self.STATUS.keys() else user_status
    

    def get_profile_picture(self):
        """Get the User object's profile picture."""
        return tk.PhotoImage(file=self.user_pf, height=35, width=35)
    
    def set_profile_picture(self, user_pf: str):
        """
        Parameters
        ----------
        user_pf : str
            The new path to the User object's profile picture.    
        """
        if not isinstance(user_pf, str):
            raise TypeError(f"user_pf should be of type str, got {type(user_pf)} instead")
        if user_pf == "":
            raise ValueError("User's profile picture must have a value.")
        
        self.user_pf = user_pf

    def get_username(self):
        """Gets the User object's username."""
        return self.username

    def set_username(self, username: str):
        """
        Parameters
        ----------
        username : str
            The new username for the User object.    
        """
        if not isinstance(username, str):
            raise TypeError(f"Username should be of type str, got {type(username)} instead")
        if len(username) == 0:
            raise ValueError("Username must contain at least 1 character")
        
        self.username = username
    
    def get_status(self):
        """Get the User object's status"""
        return self.user_status

    def set_status(self, status: Literal["ONLINE", "IDLE", "DND", "OFFLINE"]):
        """
        Parameters
        ----------
        status : str
            The new status of the User.

            Valid values are ONLINE, IDLE, DND, and OFFLINE    
        """
        if not status in self.STATUS.keys():
            raise ValueError(f"User status can only be set to the values ONLINE, IDLE, DND, or OFFLINE, received {status} instead")
        
        self.user_status = status
            

class UserMessage(tk.Frame) :
    

    user = None
    timestamp = ""
    message = ""

    def __init__(self, user: User, timestamp: str, message: str, *args, **kwargs) -> None:
        """
        Parameters
        ----------
        user: User
            The user that sent the message.

        timestamp: str
            When the message was sent. This string should be formatted as YYYY-MM-DDTHH:MiMi:SS
        
        message: str
            The text that the message should display.

        *args & **kwargs:
            Any arguments for the Frame object. Documentation for frame is as follows.
                Construct a frame widget with the parent MASTER.

                Valid resource names: background, bd, bg, borderwidth, class, colormap, container, cursor, 
                
                height, highlightbackground, highlightcolor, highlightthickness, relief, takefocus, visual, width.
        """
        background_color = "#31343b"
        foreground_color = "White"

        super().__init__(*args, **kwargs)
        
        # If the user sets the background then update the color for the entire frame
        if "background" in kwargs or "bg" in kwargs:
            background_color = kwargs["background"] if "background" in kwargs else kwargs["bg"]
        
        # Otherwise, set the background to the default value
        else:
            self.configure(background=background_color)
        
        # For theming purposes, setting the foreground will set it for all children.
        if "foreground" in kwargs or "fg" in kwargs:
            foreground_color = kwargs["foreground"] if "foreground" in kwargs else kwargs["fg"]
        
        
        if not isinstance(user, User):
            raise TypeError(f"User was expected to be of type User, got {type(user)} instead.")
        self.user = user

        if not isinstance(timestamp, str):
            raise TypeError(f"Timestamp should be of type string but got {type(timestamp)} instead and of format YYYY-MM-DDTHH:MiMi:SS")
        if timestamp == "":
            raise ValueError(f"Timestamp cannot be blank. Enter a timestamp of the following format YYYY-MM-DDTHH:MiMi:SS")
        self.timestamp = timestamp

        if not isinstance(message, str):
            raise TypeError(f"Message should be of type string but got {type(message)} instead")
        if message == "":
            raise ValueError(f"Message must be at least 1 character long")
        self.message = message

        # Create the profile picture label
        self.user_pf_label = tk.Label(self, image=user.get_profile_picture())
        self.user_pf_label.grid(row=0, rowspan=2, column=0, pady=3)

        # Create username label
        self.username_label = tk.Label(self, background=background_color, foreground=foreground_color, font=("Arial", 15), text=self.user.get_username(), justify="left")
        self.username_label.grid(row=0, column=1, sticky='w')

        # Create timestamp label
        self.timestamp_label = tk.Label(self, background=background_color, foreground=foreground_color, font=("Arial", 7), text=self.timestamp, justify="left")
        self.timestamp_label.grid(row=0, column=2, sticky='w')

        # Create the message label where all the user's text will go.
        self.message_label = tk.Label(self, background=background_color, foreground=foreground_color, text=self.message, wraplength=WIDTH_SCREEN-45, justify="left")
        self.message_label.grid(row=1, rowspan=5, column=1, columnspan=5, sticky='w')
    
    def grid(self, *args, **kwargs):
        
        # By default, this message will stick to the bottom left,
        # but add support for other configurations.
        if "sticky" in kwargs:
            super().grid(*args, **kwargs)
        
        else:
            super().grid(sticky='sw', *args, **kwargs)

        height_of_frame = self.username_label.winfo_reqheight() + self.message_label.winfo_reqheight()

        # Ensure that the frame is of the height it needs to be, but still lies within the chat frame.
        self.configure(height=height_of_frame, width=WIDTH_SCREEN-6)
        self.grid_propagate(0)

class EmptyMessage(tk.Frame):

    def __init__(self, *args, **kwargs) -> None:
        """
        Similar to a normal frame, used to buffer out the message box so that messages populate from bottom to top.
        EmptyMessage objects are overwritten by UserMessage objects.
        """
        super().__init__(*args, **kwargs)

        message_size = 595

        if "background" in kwargs or "bg" in kwargs:
            background_color = kwargs["background"] if "background" in kwargs else kwargs["bg"]

        else:
           background_color = "#31343b"
        
        if "height" in kwargs:
            message_size = kwargs["height"]

        self.configure(height=message_size, width=WIDTH_SCREEN-6, background=background_color)


# Code borrowed from: https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame
class ScrollableFrame(tk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    * This frame only allows vertical scrolling.
    """

    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           yscrollcommand=vscrollbar.set, height=kw["height"], width=kw["width"])
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        
        vscrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = ttk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            # Update the scrollbars to match the size of the inner frame.
            current_view = canvas.yview()[1]
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())
            
            # If the scroll bar is "close enough" to the bottom,
            # when the canvas is updated, keep the scroll bar on the bottom.
            if(current_view > 0.97):
                canvas.yview_moveto(1)

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)