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

    def __init__(self, user_pf : str, username : str, user_status: Literal["ONLINE", "IDLE", "DND", "OFFLINE"], user_status_message : str = "") -> None:
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
        self.status = self.STATUS[user_status] if user_status in self.STATUS.keys() else user_status

        self.status_message = user_status_message
    

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
        return self.status

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
        
        self.status = status
    
    def get_status_message(self):
        """Get the User object's status message"""
        return self.status_message

    def set_status(self, status_message : str):
        """
        Parameters
        ----------
        status : str
            The new status message of the User.
        """
        
        self.status = status_message
            

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

        background_color = kwargs["background"] if "background" in kwargs else kwargs["bg"] if "bg" in kwargs else "#31343b"
        message_size = kwargs["height"] if "height" in kwargs else 595

        self.configure(height=message_size, width=WIDTH_SCREEN-6, background=background_color)


class UserFrame(tk.Frame):
    
    def __init__(self, user : User, *args, **kwargs):
        """
        An object that creates a frame from a given User object.

        Parameters
        ----------
        user : User
            The user that will be used to create this UserFrame.
        
        args/kwargs
            Any values that will modify the Frame object's attributes.
            Below is the documentation:

            Construct a frame widget with the parent MASTER.

            Valid resource names: background, bd, bg, borderwidth, class, colormap, container, cursor, 
            
            height, highlightbackground, highlightcolor, highlightthickness, relief, takefocus, visual, width.
        """
        DEF_BG_COLOR = "#31343b"
        DEF_FG_COLOR = "White"
        
        super().__init__(*args, **kwargs)

        self.user = user

        # If the user sets the background then update the color for the entire frame
        background_color = kwargs["background"] if "background" in kwargs else kwargs["bg"] if "bg" in kwargs else DEF_BG_COLOR
        self.configure(background=background_color)
        
        # For theming purposes, setting the foreground will set it for all children.
        foreground_color = kwargs["foreground"] if "foreground" in kwargs else kwargs["fg"] if "bg" in kwargs else DEF_FG_COLOR

        # The user's profile picture
        self.pf_label = tk.Label(self, image=user.get_profile_picture())
        self.pf_label.grid(row=0, column=0, rowspan=3)
        
        # The label that will display the username
        self.username_label = tk.Label(self, foreground=foreground_color, background=background_color, font=("Arial", 15), text=user.get_username(), anchor='w', width=17)
        self.username_label.grid(row=1, column=1)

        # The label that will display the user's status, if applicable.
        self.status_message_label = tk.Label(self, foreground=foreground_color, background=background_color, font=("Arial", 10), text=user.get_status_message(), justify='left')
        self.status_message_label.grid(row=2, column=1, sticky='w')

    
    def check_username_color(self, color : str):
        """
        Sets the username in this label to the specified color.

        Parameters
        ----------
        color : str
            The color that the username should be set to.
        """
        if not isinstance(color, str):
            raise TypeError(f"color is expected to be of type str, got {type(color)} instead")

        self.username_label.configure(foreground=color)

class RoleFrame(tk.Frame):

    def __init__(self, role_name : str, button_function, role_color : str = "White", *args, **kwargs) -> None:
        """
        The header for displaying user categories or roles.
        
        Parameters
        ----------
        role_name : str
            The name that the frame will display.
        
        button_function : function
            The function that a given button in this frame will call
        
        role_color : str
            The color that the role will use.
        
        args/kwargs
            Any values that will modify the Frame object's attributes.
            Below is the documentation:

            Construct a frame widget with the parent MASTER.

            Valid resource names: background, bd, bg, borderwidth, class, colormap, container, cursor, 
            
            height, highlightbackground, highlightcolor, highlightthickness, relief, takefocus, visual, width.
        """
        DEF_BG_COLOR = "#31343b"
        DEF_FG_COLOR = "White"
        
        super().__init__(*args, **kwargs)

        self.role_name = role_name
        self.role_color = role_color
        self.childrenlist = list()
        self.buttonlist = list()
        self.button_function = button_function

        # If the user sets the background then update the color for the entire frame
        background_color = kwargs["background"] if "background" in kwargs else kwargs["bg"] if "bg" in kwargs else DEF_BG_COLOR
        self.configure(background=background_color)
        
        # For theming purposes, setting the foreground will set it for all children.
        foreground_color = kwargs["foreground"] if "foreground" in kwargs else kwargs["fg"] if "bg" in kwargs else DEF_FG_COLOR

        # grid_propagate seems to behave very bizarrely with this object, so we're just adding this to simulate the size it needs to be.
        tk.Label(self, height=1, width=kwargs["width"] if "width" in kwargs else 40, background=background_color).grid(row=0, column=0, sticky='w')

        # The role name's label
        self.role_label = tk.Label(self, text=f"{role_name} ─ 0", foreground=foreground_color, background=background_color, font=("Arial", 10))
        self.role_label.grid(row=1, column=0, sticky='w')
    

    def add_users(self, users : User | list[User]) -> None:
        """
        Add 1 or more users to this RoleFrame.

        Parameters
        ----------
        users: User | list[User]
            The user or list of users to be added to the RoleFrame
        """

        def add_user(self : RoleFrame, user : User) -> None:
            """
            Adds a single user to the RoleFrame.

            Parameters
            ----------
            self : RoleFrame
                The RoleFrame that the UserFrame will be added to.

            user : User
                The user to be added to the RoleFrame
            """
            frame = UserFrame(user, master=self)
            frame.check_username_color(self.role_color)
            self.childrenlist.append(frame)
            frame.grid(row=len(self.childrenlist) + 1, column=0, sticky='w')
            self.role_label.configure(text=f"{self.role_name} ─ {len(self.childrenlist)}")

            mention_button = tk.Button(frame, text="M", command=lambda: self.button_function(user.username))
            mention_button.grid(row=0, column=2, rowspan=3)
            self.buttonlist.append(mention_button)

        # If there is a list, send each user into the add_user function
        if isinstance(users, list):
            for user in users:
                add_user(self, user)

        elif isinstance(users, User):
            add_user(self, users)
        
        else:
            raise TypeError(f"Expected users to be of type User or list[User], got {type(users)} instead")

    def remove_users(self, users : User | str | list[User|str]) -> None:
        """
        Removes the first occurence of the User object or string or a list of either User objects or strings

        Parameters
        ----------
        users : User | str | list[User|str]
            The list of users to be removed from the RoleFrame.
            Strings should be the username of the User to be removed

            The list may have both User objects and strs.
        """

        def remove_user(self, user : User | str) -> None:
            """
            Removes the first occurence of the User object or string within the UserFrame.

            Parameters
            ----------
            user : User | str
                The user to be removed from the RoleFrame.
                Strings should be the username of the User to be removed.
            """
            username = user

            if isinstance(user, User):
                username = user.get_username()
            
            for i in range(len(self.childrenlist)):
                if self.childrenlist[i].user.get_username() == username:
                    self.childrenlist[i].grid_forget()
                    self.childrenlist.remove(self.childrenlist[i])
                    self.buttonlist.remove(self.buttonlist[i])

                    break
        
        # If there is a list, send each user into the remove_user function
        if isinstance(users, list):
            for user in users:
                remove_user(self, user)

        elif isinstance(users, User) or isinstance(users, str):
           remove_user(self, users)

        else:
            raise TypeError(f"Expected users to be of type User, str, or list[User|str], got {type(users)} instead")
        
        # Reset the RoleFrame so that the children start from the top of the list
        for child in self.childrenlist:
            child.grid_forget()
        
        for i in range(len(self.childrenlist)):
            self.childrenlist[i].grid(row=i + 2, column=0, sticky='w')
        
        # Update the number of users in the RoleFrame
        self.role_label.configure(text=f"{self.role_name} ─ {len(self.childrenlist)}")


# Code borrowed from: https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame
class ScrollableFrame(tk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    * This frame only allows vertical scrolling.
    """

    def __init__(self, parent, background = "#31343b", *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        vscrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           yscrollcommand=vscrollbar.set, height=kw["height"], width=kw["width"], background=background)
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