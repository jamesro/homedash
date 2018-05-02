import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGroupBox, QVBoxLayout, QGridLayout
from weather import WeatherWidget
from busstop import BusStopWidget
from clock import ClockWidget


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
        # p.setColor(self.backgroundRole(), Qt.black)
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

        layout.addWidget(ClockWidget(), 0, 3, 3, 3)
        layout.addWidget(WeatherWidget(), 1, 0, 2, 3)
        layout.addWidget(BusStopWidget(), 2, 0, 2, 2)

        self.horizontalGroupBox.setLayout(layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet('QLabel{color: #fff;}')
    app.setStyleSheet("QStatusBar::item { border: 0px solid black }; ")
    ex = App()
    sys.exit(app.exec())
