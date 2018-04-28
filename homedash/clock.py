from PyQt5.QtWidgets import QLCDNumber, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5 import QtGui
from datetime import datetime


class ClockWidget(QWidget):

    def __init__(self):
        super().__init__()

        # VBox
        vbox = QVBoxLayout()
        clock = DigitalClock()
        date = Date()

        vbox.addWidget(clock)
        vbox.addWidget(date)
        self.setLayout(vbox)


class DigitalClock(QLCDNumber):

    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        # Font
        self.font = QtGui.QFont()
        self.font.setPointSize(25)
        self.setFont(self.font)
        # get the palette
        palette = self.palette()
        # "light" border
        palette.setColor(palette.Light, Qt.black)
        # "dark" border
        palette.setColor(palette.Dark, Qt.black)

        # set the palette
        self.setPalette(palette)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self.showTime()

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)


class Date(QLabel):

    def __init__(self):
        super().__init__()

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(60000)  # 1 minute

        self.update()

    def update(self):
        current_date = datetime.now().strftime("%B %d, %Y")
        self.setText(current_date)
