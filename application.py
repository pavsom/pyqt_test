from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QColor, QFont

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test Application")

        button = QPushButton("Test button")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setMinimumSize(QSize(250, 190))
        self.setMaximumSize(QSize(777, 666))
        self.setFont(QFont("Times", 10))

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Button clicked...")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
