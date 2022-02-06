from tkinter import Tk, Canvas, PhotoImage, Button, Entry, StringVar

from ui.asset_manager import AssetType

WINDOW_WIDTH = 1015
WINDOW_HEIGHT = 717

BACKGROUND_COLOR = "#ffffff"
CANVAS_COLOR = "#ffffff"
ENTRY_BG_COLOR = "#00C1FF"

class PeakWindow(Tk):
    """Main Application subclass of `Tk`"""

    def __init__(self, asset_man, *args, **kwargs):
        """Initializes our window"""

        self.asset_man = asset_man

        # Init parent class
        super().__init__(
            *args,
            **kwargs
        )

        # Set window title
        self.title("Peak")
        
        # Set window size
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        # Set initial state
        self.canvas = None
        self.bg_image = None

    def add_buttons(self):
        """Adds buttons"""
        
        # Add home button
        self.button_home_image = PhotoImage(file=self.asset_man.get_path(AssetType.BUTTON_HOME))
        self.button_home = Button(
            image=self.button_home_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("home button click!"),
            relief="flat"
        )
        self.button_home.place(
            x=20,
            y=238,
            width=41,
            height=34
        )
        
        # Add user button
        self.button_user_image = PhotoImage(file=self.asset_man.get_path(AssetType.BUTTON_USER))
        self.button_home = Button(
            image=self.button_user_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("user button click!"),
            relief="flat"
        )
        self.button_home.place(
            x=17,
            y=302,
            width=47,
            height=55
        )

        # Add settings button
        self.button_settings_image = PhotoImage(file=self.asset_man.get_path(AssetType.BUTTON_SETTINGS))
        self.button_settings = Button(
            image=self.button_settings_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("settings button click!"),
            relief="flat"
        )
        self.button_settings.place(
            x=20,
            y=387,
            width=43,
            height=48
        )
        
    def add_status_cards(self):
        # Draw instagram card
        self.instagram_card_bg = PhotoImage(file=self.asset_man.get_path(AssetType.INSTAGRAM_CARD))
        self.instagram_card_button = Button(
        	image=self.instagram_card_bg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('instagram card button'),
            relief="flat"
        )
        self.instagram_card_button.place(
        	x=126,
            y=472,
            width=185,
            height=175
        )
        
        # Draw whatsapp card
        self.whatsapp_card_bg = PhotoImage(file=self.asset_man.get_path(AssetType.WHATSAPP_CARD))
        self.whatsapp_card_button = Button(
        	image=self.whatsapp_card_bg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('whatsapp card button'),
            relief="flat"
        )
        self.whatsapp_card_button.place(
        	x=346,
            y=477,
            width=190,
            height=170
        )
        
        # Draw facebook card
        self.facebook_card_bg = PhotoImage(file=self.asset_man.get_path(AssetType.FACEBOOK_CARD))
        self.facebook_card_button = Button(
        	image=self.facebook_card_bg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('facebook card button'),
            relief="flat"
        )
        self.facebook_card_button.place(
        	x=551,
            y=480,
            width=203,
            height=172
        )
        
        # Draw twitter card
        self.twitter_card_bg = PhotoImage(file=self.asset_man.get_path(AssetType.TWITTER_CARD))
        self.twitter_card_button = Button(
        	image=self.twitter_card_bg,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print('twitter card button'),
            relief="flat"
        )
        self.twitter_card_button.place(
        	x=776,
            y=485,
            width=197,
            height=167
        )
    
    def add_entry(self):
        # Draw text field entry
        self.entry_bg_image = PhotoImage(file=self.asset_man.get_path(AssetType.ENTRY_BACKGROUND))
        self.entry_bg = self.canvas.create_image(
            543,
            331,
            image=self.entry_bg_image
        )

        # Add entry
        self.entry_text = StringVar()
        self.entry_text.set("saharaa.in")
        self.entry = Entry(
            bd=0,
            bg=ENTRY_BG_COLOR,
            highlightthickness=0,
            textvariable=self.entry_text
        )
        self.entry.place(
            x=238,
            y=294,
            width=610,
            height=72
        )
        
        # Add search button
        self.button_go_image = PhotoImage(file=self.asset_man.get_path(AssetType.BUTTON_GO))
        self.button_go = Button(
        	image=self.button_go_image,
            borderwidth=0,
            highlightwidth=0,
            command=lambda: print("go button clicked"),
            relief="flat"
        )
        self.button_go.place(
        	x=734,
            y=299,
            width=132,
            height=65
        )
    
    def create_canvas(self):
        """Creates and draws on the canvas"""

        # Create a canvas
        self.canvas = Canvas(
            self,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            bd=0,
            bg=CANVAS_COLOR,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0) # place canvas at the starting point of 0, 0
        
        # Draw background white
        self.bg_white_image = PhotoImage(file=self.asset_man.get_path(AssetType.BACKGROUND_WHITE))
        self.canvas.create_image(
            543,
            358,
            image=self.bg_white_image
        )
        
        # Draw background image
        self.bg_image = PhotoImage(file=self.asset_man.get_path(AssetType.BACKGROUND))
        self.canvas.create_image(
            507,
            358,
            image=self.bg_image
        )
        
    def widgets(self):
        """Add all the widgets here"""

        self.create_canvas()
        self.canvas.pack()

        self.add_status_cards()
        self.add_entry()
        self.add_buttons()

    def setup(self):
        """Setup the application"""

        self.configure(bg=BACKGROUND_COLOR)

    def run(self):
        self.widgets()
        self.mainloop()