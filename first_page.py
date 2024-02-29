from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sys
import requests
from datetime import datetime, timedelta


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load UI File
        uic.loadUi("weather1.ui", self)
        self.setFixedSize(461, 571)

        self.main_window = None

        # Our Widgets
        self.city = self.findChild(QLineEdit, "city_name")
        self.search = self.findChild(QPushButton, "search_button")

        # Our Widgets Actions
        self.search.clicked.connect(self.clicker)

        # Showing Window
        self.show()

    # Function To click button
    def clicker(self):
        city = self.city.text()
        self.main_window = Main(city)
        self.main_window.show()


class Main(QMainWindow):
    def __init__(self, city):
        super(Main, self).__init__()
        uic.loadUi("weather2.ui", self)
        self.setFixedSize(461, 571)
        self.API_KEY = "b922f55b4465c11b31b2101ab35f4243"
        self.city = city

        # Find UI elements
        self.pic = self.findChild(QLabel, "pic")
        self.temp_today = self.findChild(QLabel, "temp_today")
        self.weather_icon = self.findChild(QLabel, "weather_sit")
        self.situation = self.findChild(QLabel, "situation")
        self.city_name = self.findChild(QLabel, "city")
        self.today = self.findChild(QLabel, "today")
        self.month = self.findChild(QLabel, "month")
        self.day = self.findChild(QLabel, "day")
        self.hour = self.findChild(QLabel, "hour")
        self.minute = self.findChild(QLabel, "minute")
        self.tomorrow = self.findChild(QLabel, "tomorrow")
        self.weather_tomorrow = None
        self.temperature_tomorrow = None

        # Write City Name
        self.city_title = self.city.title()
        self.city_name.setText(self.city_title)

        # --------------- Image Section -----------------
        """Weather Situation"""
        self.sunny_day = QPixmap("images/Sun.png")
        self.night = QPixmap("images/Blood.png")
        self.evening = QPixmap("images/evening.jpg")

        # Weather images
        self.sun = QPixmap("images/Sun.png")
        self.rain = QPixmap("images/rain.png")
        self.cloud = QPixmap("images/clouds.png")

        # -------------- Date and Time Section -----------
        """DateTime Use"""
        self.date = datetime.now()
        self.tomorrow_day = self.date + timedelta(1)
        self.tomorrow_date = self.tomorrow_day.strftime("%Y-%m-%d")

        """Our Widgets Action"""
        self.today.setText(self.date.strftime("%A"))
        self.tomorrow.setText(self.tomorrow_day.strftime("%A"))
        self.month.setText(self.date.strftime("%b"))
        self.day.setText(self.date.strftime("%d"))
        self.hour.setText(self.date.strftime("%H"))
        self.minute.setText(self.date.strftime("%M"))

        """Day Or Night"""
        if 5 <= int(self.date.strftime("%H")) <= 16:
            self.pic.setPixmap(self.sunny_day)
        elif 17 <= int(self.date.strftime("%H")) <= 19:
            self.pic.setPixmap(self.evening)
        else:
            self.pic.setPixmap(self.night)

        # Fetch and display weather information
        self.fetch_weather()

        self.show()

    def fetch_weather(self):
        try:
            response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.API_KEY}&units=metric"
            )
            response.raise_for_status()

            weather_data = response.json()
            weather_main = weather_data["weather"][0]["main"]
            temp_today = int(weather_data["main"]["temp"])

            if weather_main == "Sun":
                self.weather_icon.setPixmap(self.sun)
            elif weather_main == "Clouds":
                self.weather_icon.setPixmap(self.cloud)
            elif weather_main == "Rain":
                self.weather_icon.setPixmap(self.rain)

            self.temp_today.setText(str(temp_today))
            self.situation.setText(weather_main)

            """Using API for weather Tomorrow"""
            response_tomorrow = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.API_KEY}&units"
                f"=metric&date={self.tomorrow_date}")
            self.weather_tomorrow = response_tomorrow.json()["weather"][0]["main"]
            self.temperature_tomorrow = int(response_tomorrow.json()["main"]["temp"])

            "Set To tomorrow Label"
            self.temp_tomorrow.setText(str(self.temperature_tomorrow))
            self.situation_tomorrow.setText(self.weather_tomorrow)
        except requests.exceptions.RequestException as e:
            print("Error fetching weather data:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())
