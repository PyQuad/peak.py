import time

from tkinter import Tk, Canvas, PhotoImage, Button, Entry, StringVar, Label
from tkinter.font import Font

from asset_manager import AssetType
from network import ping_url

WINDOW_WIDTH = 1015
WINDOW_HEIGHT = 717

POPULAR_POLL_INTERVAL = 10

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

        # Make the window non-resizable
        self.resizable(False, False)

        # Define popular urls
        self.popular_urls = [
            ("instagram", "https://instagram.com"),
            ("whatsapp", "https://whatsapp.com"),
            ("facebook", "https://facebook.com"),
            ("twitter", "https://twitter.com")
        ]

        # Set initial state
        self.is_popular_loop_running = True
        self.canvas = None
        self.bg_image = None

    def terminate_popular_loop(self):
        self.is_popular_loop_running = False

    def update_popular(self):
        for name, url in self.popular_urls:
            resp = ping_url(url)

            result = None
            error = None
            try:
                result = resp["message"]
            except KeyError:
                error = resp["error"]

            if error:
                to_add = "An error occured"
                print(error)
            else:
                status = result["status"]
                reason = result["reason"]
                ping = round(result["ping"], 3)

                is_working = "Working smoothly!" if status <= 200 else "Something's wrong"
                to_add = f"[{is_working}]\n\nStatus: {status}\nReason: {reason}\nPing: {ping}"

            match name:
                case "instagram":
                    self.instagram_card_label_text.set(to_add)
                case "whatsapp":
                    self.whatsapp_card_label_text.set(to_add)
                case "facebook":
                    self.facebook_card_label_text.set(to_add)
                case "twitter":
                    self.twitter_card_label_text.set(to_add)

    def update_popular_loop(self):
        while True:
            if not self.is_popular_loop_running:
                return

            time.sleep(POPULAR_POLL_INTERVAL) # sleep for a certain amount of seconds before checking again
            self.update_popular()

    def on_go_click(self):
        """Handles on click event for go button"""

        url = self.entry_text.get()
        resp = ping_url(url)

        result = None
        error = None
        try:
            result = resp["message"]
        except KeyError:
            error = resp["error"]

        if error:
            self.result_text.set(error)
            return

        status = result["status"]
        reason = result["reason"]
        ping = round(result["ping"], 3)

        #to_show = f"Status: {status}\nReason: {reason}\nPing: {ping}"
        to_show = ""
        to_show += " Status    Ping   Reason  "
        to_show += "\n ──────────────────────── "
        to_show += f"\n     {status}     {ping}     {reason}       "

        self.result_text.set(to_show)

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
            height=33.1
        )
        
        # Add user button
        self.button_user_image = PhotoImage(file=self.asset_man.get_path(AssetType.BUTTON_USER))
        self.button_user = Button(
            image=self.button_user_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("user button click!"),
            relief="flat"
        )
        self.button_user.place(
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
    
    def add_status_labels(self):
        # Instagram
        self.instagram_card_label_text = StringVar()
        self.instagram_card_label = Label(
            textvariable=self.instagram_card_label_text,
            bg="white",
            fg="black"
        )

        self.instagram_card_label.place(
        	x=137,
            y=545,
        )
        self.instagram_card_label.lift()

        # Whatsapp
        self.whatsapp_card_label_text = StringVar()
        self.whatsapp_card_label = Label(
            textvariable=self.whatsapp_card_label_text,
            bg="white",
            fg="black"
        )

        self.whatsapp_card_label.place(
            x=377,
            y=545
        )
        self.whatsapp_card_label.lift()

        # Facebook
        self.facebook_card_label_text = StringVar()
        self.facebook_card_label = Label(
            textvariable=self.facebook_card_label_text,
            bg="white",
            fg="black"
        )

        self.facebook_card_label.place(
            x=577,
            y=545
        )
        self.facebook_card_label.lift()

        # Twitter
        self.twitter_card_label_text = StringVar()
        self.twitter_card_label = Label(
            textvariable=self.twitter_card_label_text,
            bg="white",
            fg="black"
        )

        self.twitter_card_label.place(
            x=800,
            y=545
        )
        self.twitter_card_label.lift()

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
            height=165
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

        self.add_status_labels()
    
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
        self.entry_text.set("https://saharaa.in") # keep default
        self.entry = Entry(
            bd=0,
            bg=ENTRY_BG_COLOR,
            highlightthickness=0,
            textvariable=self.entry_text,
            fg="white",
            font=Font(size=14)
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
            highlightthickness=0,
            command=self.on_go_click,
            relief="flat"
        )
        self.button_go.place(
        	x=734,
            y=299,
            width=132,
            height=65
        )
   
    def add_result_text(self):
        self.result_text = StringVar()
        self.result_label = Label(textvariable=self.result_text, bg="white")

        self.result_label.configure(anchor="center")

        self.result_label.place(
            x=5 * (WINDOW_WIDTH // 10),
            y=6.3 * (WINDOW_HEIGHT // 11),
            anchor="center"
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
    
    def after_widgets(self):
        """Runs after UI widgets are laid out successfully"""

        # Set cards text to loading at start
        self.instagram_card_label_text.set("\n    Hold on. Calculating...")
        self.whatsapp_card_label_text.set("\nHold on. Calculating...")
        self.facebook_card_label_text.set("\nHold on. Calculating...")
        self.twitter_card_label_text.set("\nHold on. Calculating...")

    def widgets(self):
        """Add all the widgets here"""

        self.create_canvas()
        self.canvas.pack()

        self.add_status_cards()
        self.add_entry()
        self.add_buttons()
        self.add_result_text()

    def setup(self):
        """Setup the application"""

        self.configure(bg=BACKGROUND_COLOR)

    def run(self):
        self.setup()
        self.widgets()

        self.after(10, self.after_widgets)

        self.mainloop()
