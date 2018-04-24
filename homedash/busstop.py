from urllib.request import urlopen, urlretrieve
from PyQt5.QtWidgets import QLayout, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont
import json

class BusStopWidget(QWidget):

    def __init__(self):
        super().__init__()
        
        self.data = self.get_bus_data()







    def get_bus_data(self):
        response = urlopen(self.url).read().decode('utf-8')
        return json.loads(response)

