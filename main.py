from PyQt5.QtWidgets import QApplication
import sys
from window import PeakWindow

if __name__ == "__main__":
    # Create a QApplication
    app = QApplication(sys.argv)

    # Create a window
    window = PeakWindow()

    # Show window
    window.show()

    # Handle process exit
    sys.exit(app.exec_())
