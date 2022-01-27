from tkinter import Tk, Canvas, PhotoImage, Button, Entry, StringVar

from asset_manager import AssetType

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
            y=120,
            width=40,
            height=44
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

        # Draw background image
        self.bg_image = PhotoImage(file=self.asset_man.get_path(AssetType.BACKGROUND))
        self.canvas.create_image(
            617,
            474,
            image=self.bg_image
        )

        # Draw status cards
        self.status_image = PhotoImage(file=self.asset_man.get_path(AssetType.STATUS_CARDS))
        self.canvas.create_image(
            548,
            562,
            image=self.status_image
        )

        # Draw text field entry
        self.entry_bg_image = PhotoImage(file=self.asset_man.get_path(AssetType.ENTRY))
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

    def widgets(self):
        """Add all the widgets here"""

        self.create_canvas()
        self.canvas.pack()

        self.add_buttons()

    def setup(self):
        """Setup the application"""

        self.configure(bg=BACKGROUND_COLOR)

    def run(self):
        self.widgets()
        self.mainloop()