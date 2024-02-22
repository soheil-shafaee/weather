from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load UI File
        uic.loadUi("weather1.ui", self)
        self.setFixedSize(461, 571)

        # Our Widgets
        self.city = self.findChild(QLineEdit, "city_name")
        self.search = self.findChild(QPushButton, "search_button")

        # Our Widgets Actions
        self.search.clicked.connect(self.clicker)

        # Showing Window
        self.show()

    # Function To click button
    def clicker(self):
        return self.city.text()


app = QApplication(sys.argv)
UiWindow = UI()
app.exec_()
