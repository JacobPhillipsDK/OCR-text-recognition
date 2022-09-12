import sys

from PyQt6.QtWidgets import QStatusBar
from PySide6.QtCore import QSize
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMessageBox, QApplication, QMainWindow, QPushButton, QLabel, QToolBar
from PySide6.QtCore import Qt
import qtawesome as qta

window_title = "Screen shot snipping tool"  # Window title

window_width = 500  # Window width
window_height = 350  # Window height
window_size = QSize(window_width, window_height)  # Window size


# Subclass QMainWindow to customize your application's main window
class SnippingWidgetTool(QMainWindow):
    def __init__(self):
        super().__init__()  # Call the inherited classes __init__ method
        self.setWindowTitle(window_title)  # Set the window's title
        self.setFixedSize(window_size)  # Set the window's size
        self.counter = 0

        # Initialize elements
        self.toolbar = QToolBar("My toolbar")
        self.text = QLabel("This is a text", self)

        # Call functions
        self.information_text()  # Call the information text method
        self.snippet_button()  # Call the screenshot button method

    def snippet_button(self):
        # Screenshot button
        self.button = QPushButton("Snip Tool", self)  # Create a button in the window || Initialize the button
        # -- Clickable actions --
        self.button.clicked.connect(self.the_button_was_clicked)  # Connect the button to the function
        # --- Reizing the button ---
        # Center the button position at the top of the window relative to the window size
        self.button.move(int((window_width / 2) - window_width / 2),
                         int((window_height / 2) - window_height / 2)+180)  # Set the button's position
        self.button.resize(window_width, 50)  # Set the button's size

    def increase_counter(self):
        self.counter += 1
        print(f' Counter is now: {self.counter}')

    def the_button_was_clicked(self):
        self.increase_counter()
        self.button.setText(f"You have clicked on me  {self.counter}")  # Change the button's text
        self.text.setText(f"You have clicked on me  {self.counter}")  # Change the button's text
        self.setWindowTitle(f"Clicked {self.counter} times")  # Change the window's title

    def information_text(self):
        self.text.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt
                               .AlignmentFlag.AlignVCenter)
        self.setCentralWidget(self.text)






def main():
    app = QApplication(sys.argv)  # Create an instance of QApplication
    window = SnippingWidgetTool()  # Instantiate your custom class
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.
    app.exec()  # Start the application


if __name__ == '__main__':  # Run the application
    main()  # Run the main function
