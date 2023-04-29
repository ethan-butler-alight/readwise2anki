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

        # Label to display the current highlight you are on
        highlight_num = QLabel("1 / 20")
        grid.addWidget(highlight_num, 0, 0)

        # Label to show which specific source the highlight came from(name of book, article, etc.)
        source = QLabel("Introduction to Algorithms")
        grid.addWidget(source, 1, 0)

        # Label to show which number highlight from the current source you are on
        source_num = QLabel("1 / 2")
        grid.addWidget(source_num, 1, 1)

        # Label to show the actual highlight itself
        highlight = QLabel("Here is an example highlight")
        grid.addWidget(highlight, 2, 0)

        # Textbox for creating the front of a card
        front = QTextEdit()
        grid.addWidget(front, 3, 0)

        # Textbox for creating the back of the card
        back = QTextEdit()
        grid.addWidget(back, 4, 0)

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

# TODO: Make a user option to autocopy the current highlight to the clipboard
