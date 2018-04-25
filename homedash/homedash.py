import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QTabWidget, QVBoxLayout, QLCDNumber, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QDate, QTime, QDateTime, Qt, QTimer
from PyQt5 import QtGui
from weather import WeatherWidget
from busstop import BusStopWidget

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'HomeDash'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.setCentralWidget(self.horizontalGroupBox)
        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()

        layout.addWidget(DigitalClock(), 0, 3, 3, 3)
        layout.addWidget(DigitalClock(), 0, 0, 1, 2)
        layout.addWidget(DigitalClock(), 0, 2, 1, 1)
        layout.addWidget(WeatherWidget(), 1, 0, 2, 3)
        layout.addWidget(BusStopWidget(), 2, 0, 2, 2)

        self.horizontalGroupBox.setLayout(layout)


class DigitalClock(QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        self.setSegmentStyle(QLCDNumber.Filled)

        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        # get the palette
        palette = self.palette()

        # foreground color
        palette.setColor(palette.WindowText, Qt.white)
        # background color
        palette.setColor(palette.Background, Qt.black)

        # set the palette
        self.setPalette(palette)
        self.showtime()

    def showtime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        self.display(text)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('QLabel{color: #fff;}')
    ex = App()
    sys.exit(app.exec())
