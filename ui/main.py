import time

from threading import Thread

from window import PeakWindow
from asset_manager import AssetManager

if __name__ == "__main__":
    # Load the asset manager
    asset_man = AssetManager()

    # Create a Tkinter application
    root = PeakWindow(asset_man)

    # Create a thread
    ping_popular_thread = Thread(target=root.update_popular_loop)

    # Start the thread
    ping_popular_thread.start()

    # Run application
    root.run()

    # End the background thread once tkinter window exits
    root.terminate_popular_loop()
