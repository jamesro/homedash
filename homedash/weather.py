from urllib.request import urlopen, urlretrieve
import json
import os.path
from PyQt5.QtWidgets import QLayout, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont


id = None
key = None
url = None

def getcurrentweather():
    # response = urlopen(url).read().decode('utf-8')
    # obj = json.loads(response)
    # name = obj['city']['name']
    # details = []
    pass

def write_data():
    pass


class WeatherWidget(QWidget):

    def __init__(self):
        super().__init__()

        # Temporary workaround to avoid hitting API request limit
        with open('../data/weather.json') as f:
            data = json.load(f)

        self.city = data['name']
        self.weather_description = data['weather'][0]['description']
        self.temp = data['main']['temp']

        # Weather icon
        icon_code = data['weather'][0]['icon']
        self.icon_location = self.get_icon(icon_code)

        # Fonts
        city_font = QFont("Times", 15, QFont.Bold)

        # VBox
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        city_label = QLabel()
        city_label.setFont(city_font)
        city_label.setText(self.city)
        vbox.addWidget(city_label)
        vbox.addWidget(QLabel("Temp : {}°C".format(round(self.temp - 273.15))))
        icon = QLabel()
        icon.setGeometry(10, 10, 800, 800)
        icon.setPixmap(QPixmap(self.icon_location))
        vbox.addWidget(icon)
        vbox.addWidget(QLabel(self.weather_description))
        self.setLayout(vbox)

    def get_icon(self, icon_code):
        if not os.path.isfile("../data/weather_icons/{}.png".format(icon_code)):
            url = "http://openweathermap.org/img/w/" + str(icon_code) + ".png"
            urlretrieve(url, "../data/weather_icons/{}.png".format(icon_code))

        return "../data/weather_icons/{}.png".format(icon_code)
