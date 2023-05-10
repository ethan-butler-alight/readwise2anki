# import the main window object (mw) from aqt
from aqt import mw, AnkiQt
from aqt.addcards import AddCards

# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect

# import all of the Qt GUI library
from aqt.qt import *

# Import readwise module
from . import readwise


class Highlights:
    def __init__(self):
        self.highlight = None

    def get_current_highlight(self):
        """Get the current highlight and its associated information"""
        pass


# This is a reference I found useful for PyQt6: https://www.pythonguis.com/pyqt6-tutorial/


class GUIFromScratch(QMainWindow):
    """Class that acts as the main GUI for the addon"""

    def __init__(self, mw: AnkiQt) -> None:
        # Fetch the data from Readwise
        self.account = readwise.Readwise()
        self.data = self.account.data
        self.highlight_number = self.account.total_highlights

        # Save the first highlight's information
        source = "Source"
        highlight = "Highlight"

        # Calls the QWidget constructor and pass the main window as the parent
        QWidget.__init__(self, mw)

        # Update the window's title
        self.setWindowTitle("Import from Readwise")

        # Set the window's dimensions
        self.setMinimumWidth(600)
        self.setMinimumHeight(450)

        # Create a grid layout
        grid = QGridLayout()

        # Fonts
        title_font = QFont("Arial", 24, QFont.Weight.Bold)

        # CREATE THE WIDGETS
        # Highlight widgets
        highlight_label = QLabel("Highlight")
        highlight_label.setFont(title_font)
        source_label = QLabel(f"Source: {source}")

        highlight_content = QLabel(highlight)
        previous_highlight = QPushButton("Previous")
        highlight_number = QLabel(f"1 / {self.highlight_number}")
        next_highlight = QPushButton("Next")

        # Card Type Widgets
        type_label = QLabel("Type")
        type_button = QPushButton("Basic")

        # Deck Widgets
        deck_label = QLabel("Deck")
        deck_button = QPushButton("Test")

        # Card Input
        front_label = QLabel("Front")
        front_input = QTextEdit("")
        back_label = QLabel("Back")
        back_input = QTextEdit("")
        tags_label = QLabel("Tags")
        tags_input = QTextEdit("Tags")

        # Bottom Buttons
        help_button = QPushButton("Help")
        add_button = QPushButton("Add")
        close_button = QPushButton("Close")

        # PLACE THE WIDGETS
        # Highlight widgets
        grid.addWidget(highlight_label, 0, 0)
        grid.addWidget(source_label, 1, 0)
        grid.addWidget(highlight_content, 2, 0)
        grid.addWidget(previous_highlight, 3, 0)
        grid.addWidget(highlight_number, 3, 1)
        grid.addWidget(next_highlight, 3, 2)

        # Card Type Widgets
        grid.addWidget(type_label, 4, 0)
        grid.addWidget(type_button, 4, 1)

        # Deck Widgets
        grid.addWidget(deck_label, 4, 2)
        grid.addWidget(deck_button, 4, 3)

        # Card Input
        grid.addWidget(front_label, 5, 0)
        grid.addWidget(front_input, 6, 0, 1, 4)
        grid.addWidget(back_label, 7, 0)
        grid.addWidget(back_input, 8, 0, 1, 4)
        grid.addWidget(tags_label, 9, 0)
        grid.addWidget(tags_input, 10, 0, 1, 4)

        # Bottom Buttons
        grid.addWidget(help_button, 11, 0)
        grid.addWidget(add_button, 11, 1)
        grid.addWidget(close_button, 11, 2)

        # Create a container to hold the layout
        container = QWidget()
        container.setLayout(grid)

        # Place the container in the center of the window
        self.setCentralWidget(container)

        # Display the window
        self.show()

        # Focus the window
        self.setFocus()


class GUIFromBase(AddCards):
    """Class that acts as the main GUI for the addon that adds to the builtin AddCards window"""

    # Currently this is kept here as reference. Attempting to work on GUIFromScratch

    # TODO: Try to position the new UI elements above the built-in elements

    def __init__(self, mw: AnkiQt) -> None:
        # Call the AddCards constructor which creates the normal window responsible for adding new cards
        super().__init__(mw)

        # Get the current layout from the AddCards window
        layout = self.layout()

        # Label to display the current highlight you are on
        highlight_num = QLabel("1 / 20")
        layout.addWidget(highlight_num)

        # Update the window's title
        self.setWindowTitle("Import from Readwise")

        # Set the window's dimensions
        self.setMinimumWidth(750)
        self.setMinimumHeight(750)

        # Show the addon window
        self.show()


def menu() -> None:
    """Display the menu to import from Readwise"""
    # sel = readwise.fetch_from_export_api()

    # showInfo(data[0][0])
    # GUIFromBase(mw)
    GUIFromScratch(mw)


# TODO: get highlights from readwise

# create a new menu item, "Readwise Import"
action = QAction("Import from Readwise", mw)

# set it to call menu when it's clicked
qconnect(action.triggered, menu)

# and add it to the tools menu
mw.form.menuTools.addAction(action)

# TODO: Make a user option to autocopy the current highlight to the clipboard
