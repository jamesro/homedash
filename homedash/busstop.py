from urllib.request import urlopen, urlretrieve
from PyQt5.QtWidgets import QLayout, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QFont
import json
from datetime import datetime

class BusStopWidget(QWidget):

    def __init__(self):
        super().__init__()
        with open("../privatekeys.json") as f:
            info = json.load(f)
        self.app_id = info["busstop"]["app_id"]
        self.app_key = info["busstop"]["app_key"]
        self.url = "https://api.tfl.gov.uk/StopPoint/490012916S/arrivals?app_id={0}&app_key={1}".format(self.app_id,
                                                                                                        self.app_key)
        self.text = QLabel()
        self.text.setFont(QFont("Times", 15, QFont.Bold))
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(60000) # 60 seconds
        self.update()

    def update(self):
        response = urlopen(self.url).read().decode('utf-8')
        self.data = json.loads(response)
        time_until_bus = self.get_time_until_bus()

        self.text.setText(str(time_until_bus) + "minutes")
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(QLabel("263"))
        vbox.addWidget(self.text)
        self.setLayout(vbox)

    def get_time_until_bus(self):
        times_until_bus = []

        for data in self.data:
            arrival_time = data['expectedArrival']
            arrival_time = datetime.strptime(arrival_time, '%Y-%m-%dT%H:%M:%SZ')
            time_difference = datetime.now() - datetime.utcnow()  # UTC is annoying
            arrival_time += time_difference
            time_delta = arrival_time - datetime.now()
            times_until_bus.append((time_delta.seconds // 60)%60)

        return min(times_until_bus)