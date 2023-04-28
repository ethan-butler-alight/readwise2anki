# import the main window object (mw) from aqt
from aqt import mw, AnkiQt

# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect

# import all of the Qt GUI library
from aqt.qt import *

from . import readwise


class Highlights:
    def __init__(self):
        self.highlights = None


# This is a reference I found useful for PyQt6: https://www.pythonguis.com/pyqt6-tutorial/


class AddonGUI(QMainWindow):
    """Class that acts as the main GUI for the addon"""

    def __init__(self, mw: AnkiQt) -> None:
        # Calls the QWidget constructor and pass the main window as the parent
        QWidget.__init__(self, mw)

        # Update the window's title
        self.setWindowTitle("Import from Readwise")

        # Set the window's dimensions
        self.setMinimumWidth(750)
        self.setMinimumHeight(750)

        # Create a grid layout
        grid = QGridLayout()

        # Label to display the highlight
        highlight = QLabel("Test text")
        grid.addWidget(highlight, 0, 0)

        # Create a container to hold the layout
        container = QWidget()
        container.setLayout(grid)

        # Place the container in the center of the window
        self.setCentralWidget(container)

        # Display the window
        self.show()

        # Focus the window
        self.setFocus()


def menu() -> None:
    """Display the menu to import from Readwise"""
    # sel = readwise.fetch_from_export_api()

    # showInfo(data[0][0])
    AddonGUI(mw)


# TODO: get highlights from readwise


# create a new menu item, "Readwise Import"
action = QAction("Import from Readwise", mw)

# set it to call menu when it's clicked
qconnect(action.triggered, menu)

# and add it to the tools menu
mw.form.menuTools.addAction(action)
