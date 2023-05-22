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
        self.current_highlight_number = 0
        self.total_highlights = self.account.total_highlights

        # Save the first highlight's information
        source, highlight = self.account.get_source_and_highlight(
            self.current_highlight_number
        )

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
        self.highlight_label = QLabel("Highlight")
        self.highlight_label.setFont(title_font)
        self.source_label = QLabel(f"Source: {source}")

        self.previous_highlight = QPushButton("Previous")
        self.previous_highlight.clicked.connect(self.display_previous_highlight)

        self.highlight_number = QLabel(f"1 / {self.total_highlights}")

        self.next_highlight = QPushButton("Next")
        self.next_highlight.clicked.connect(self.display_next_highlight)

        # Card Type Widgets
        # TODO: Add these back later
        # type_label = QLabel("Type")
        # type_button = QPushButton("Basic")

        # Deck Widgets
        self.deck_label = QLabel("Deck")
        self.deck_button = QPushButton("Test")

        # Card Input
        self.front_label = QLabel("Front")
        self.front_input = QTextEdit(highlight)
        self.back_label = QLabel("Back")
        self.back_input = QTextEdit("")
        self.tags_label = QLabel("Tags")
        self.tags_input = QTextEdit("Tags")

        # Bottom Buttons
        self.help_button = QPushButton("Help")
        self.help_button.clicked.connect(self.open_help)

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_card)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close_addon)

        # PLACE THE WIDGETS
        # Highlight widgets
        grid.addWidget(self.highlight_label, 0, 0)
        grid.addWidget(self.source_label, 2, 0)
        grid.addWidget(self.previous_highlight, 3, 0)
        grid.addWidget(self.highlight_number, 3, 1)
        grid.addWidget(self.next_highlight, 3, 2)

        # Card Type Widgets
        # TODO: Add these back later
        # grid.addWidget(type_label, 4, 0)
        # grid.addWidget(type_button, 4, 1)

        # Deck Widgets
        grid.addWidget(self.deck_label, 4, 0)
        grid.addWidget(self.deck_button, 4, 1)

        # Card Input
        grid.addWidget(self.front_label, 5, 0)
        grid.addWidget(self.front_input, 6, 0, 1, 4)
        grid.addWidget(self.back_label, 7, 0)
        grid.addWidget(self.back_input, 8, 0, 1, 4)
        grid.addWidget(self.tags_label, 9, 0)
        grid.addWidget(self.tags_input, 10, 0, 1, 4)

        # Bottom Buttons
        grid.addWidget(self.help_button, 11, 0)
        grid.addWidget(self.add_button, 11, 1)
        grid.addWidget(self.close_button, 11, 2)

        # Create a container to hold the layout
        container = QWidget()
        container.setLayout(grid)

        # Place the container in the center of the window
        self.setCentralWidget(container)

        # Display the window
        self.show()

        # Focus the window
        self.setFocus()

    def display_previous_highlight(self):
        """The next highlight gets displayed on the GUI"""
        if self.current_highlight_number > 0:
            # Highlight number
            self.current_highlight_number -= 1

            # Get the source and highlight
            source, highlight = self.account.get_source_and_highlight(
                self.current_highlight_number
            )

            # Update the GUI
            self.source_label.setText(f"Source: {source}")
            self.highlight_number.setText(
                f"{self.current_highlight_number} / {self.total_highlights}"
            )
            self.front_input.setText(highlight)

    def display_next_highlight(self):
        """The next highlight gets displayed on the GUI"""
        # Highlight number
        if self.current_highlight_number < self.total_highlights:
            self.current_highlight_number += 1

            # Get the source and highlight
            source, highlight = self.account.get_source_and_highlight(
                self.current_highlight_number
            )

            # Update the GUI
            self.source_label.setText(f"Source: {source}")
            self.highlight_number.setText(
                f"{self.current_highlight_number} / {self.total_highlights}"
            )
            self.front_input.setText(highlight)

    def change_deck(self):
        pass

    def open_help(self):
        pass

    def add_card(self):
        """Add the current card to the currently selected deck"""
        pass

    def close_addon(self):
        """Close the window of the addon"""
        self.close()


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
