from PyQt5.QtWidgets import QMainWindow
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

class PeakWindow(QMainWindow):
    """Main Application subclass of `QApplication`"""

    def __init__(self, *args, **kwargs):
        """Initializes our window"""

        # Init parent class
        super().__init__(
            *args,
            **kwargs
        )

        # Set window title
        self.setWindowTitle("Peak")
        
        # Set window size
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
