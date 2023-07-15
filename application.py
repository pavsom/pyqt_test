from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont

from random import choice

import sys

window_titles = [
    'Application started',
    'Application working',
    'Application working really hard',
    'Harder then ever',
    'Doing its best',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0
        self.button_is_checked = True

        self.setWindowTitle("Test Application")

        self.button = QPushButton("Test button")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_tittle_changed)

        self.setMinimumSize(QSize(250, 190))
        self.setMaximumSize(QSize(777, 666))
        self.setFont(QFont("Times", 10))

        self.setCentralWidget(self.button)

    def the_window_tittle_changed(self, window_title):
        print("Window title changed %s" % window_title)

        if window_title == "Something went wrong":
            self.button.setDisabled(True)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)

    def the_button_was_clicked(self):
        print("Button clicked...")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked

        print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
