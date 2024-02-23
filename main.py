from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys
from datetime import datetime, timedelta


class Main(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        """Load The UI File"""
        uic.loadUi("weather2.ui", self)
        self.setFixedSize(461, 571)

        """Our Widgets"""
        self.pic = self.findChild(QLabel, "pic")
        self.temp_today = self.findChild(QLabel, "temp_today")
        self.situation = self.findChild(QLabel, "situation")
        self.city = self.findChild(QLabel, "city")
        self.today = self.findChild(QLabel, "today")
        self.month = self.findChild(QLabel, "month")
        self.day = self.findChild(QLabel, "day")
        self.hour = self.findChild(QLabel, "hour")
        self.minute = self.findChild(QLabel, "minute")
        self.tomorrow = self.findChild(QLabel, "tomorrow")
        self.situation_tomorrow = self.findChild(QLabel, "situation_tomorrow")
        self.temp_tomorrow = self.findChild(QLabel, "temp_tomorrow")

        """DateTime Use"""
        self.date = datetime.now()
        self.tomorrow_day = self.date + timedelta(1)

        """Our Widgets Action"""
        self.today.setText(self.date.strftime("%A"))
        self.tomorrow.setText(self.tomorrow_day.strftime("%A"))
        self.month.setText(self.date.strftime("%b"))
        self.day.setText(self.date.strftime("%d"))
        self.hour.setText(self.date.strftime("%H"))
        self.minute.setText(self.date.strftime("%M"))

        """Weather Situation"""
        self.sunny_day = QPixmap("images/Sun.png")
        self.night = QPixmap("images/Sun.png")
        self.evening = QPixmap("images/evening.jpg")

        """Day Or Night"""
        if 5 <= int(self.date.strftime("%H")) <= 16:
            self.pic.setPixmap(self.sunny_day)
        elif 17 <= int(self.date.strftime("%H")) <= 19:
            self.pic.setPixmap(self.evening)
        else:
            self.pic.setPixmap(self.night)

        """Showing the Window """
        self.show()


app = QApplication(sys.argv)
MainWindow = Main()
app.exec_()
