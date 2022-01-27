import sys

from tkinter import Tk

from window import PeakWindow
from asset_manager import AssetManager

if __name__ == "__main__":
    # Load the asset manager
    asset_man = AssetManager()

    # Create a Tkinter application
    root = PeakWindow(asset_man)

    # Run application
    root.run()