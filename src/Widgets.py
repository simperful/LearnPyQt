#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QWidget, QCheckBox, 
    QApplication, QPushButton, QFrame, QSlider, 
    QLabel, QProgressBar, QCalendarWidget, QVBoxLayout)
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtCore import QBasicTimer, QDate
from PyQt5.QtCore import Qt
import sys

class CheckBoxWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        cb = QCheckBox("Show Title", self)
        cb.move(20, 20)
        cb.toggle() # We have set the window title, so we also check the checkbox. 
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('QCheckBox')
        self.show()


    def changeTitle(self, state):
    # what if there is more than two checkbox, state?
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')



class ToggleButtonWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        # To create a toggle button, 
        # we create a QPushButton 
        # and make it checkable by calling the setCheckable() method. 
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)
        # We connect a clicked signal that operates with a Boolean value
        # to our user defined method.

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet('QWidget {background-color: %s}'%self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()


    def setColor(self, pressed):

        source = self.sender() # We get the button which was toggled.
        # sender is the button

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame {background-color: %s}"%self.col.name())




class SliderWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 300, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("../image/mute.png"))
        self.label.setGeometry(200, 40, 512, 512)

        self.setGeometry(300, 300, 720, 640)
        self.setWindowTitle('QSlider')
        self.show()


    def changeValue(self, value):
        
        if value == 0:
            self.label.setPixmap(QPixmap("../image/mute.png"))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap("../image/min.png"))
        elif value > 30 and value <= 80:
            self.label.setPixmap(QPixmap("../image/mid.png")) # I did not find the appropriate image
        else:
            self.label.setPixmap(QPixmap("../image/max.png")) # I did not find the appropriate image
        


class ProgressBarWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton("Start", self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("QProgressBar")
        self.show()


    def timerEvent(self, e):
    # Each QObject and its descendants have a timerEvent() event handler
        if self.step >= 100:

            self.timer.stop()
            self.btn.setText("Finished")
            return

        self.step += 1
        self.pbar.setValue(self.step)


    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText("Start")
        else:
            self.timer.start(100, self) 
            # two parameters: the timeout and 
            # the object which will receive the events
            self.btn.setText("Stop")



class CalendarWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True) 
        # what is the difference between setting true and false???
        cal.clicked[QDate].connect(self.showData)
        # If we select a date from the widget, a clicked[QDate] signal 
        # is emitted. 
        # We connect this signal to the user defined showDate() method. 

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate() # the default date is today
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Calendar")
        self.show()


    def showData(self, date):
        
        self.lbl.setText(date.toString())



if __name__ == "__main__":

    app = QApplication(sys.argv)
    # checkbox_window = CheckBoxWindow()
    # toggle_button_window = ToggleButtonWindow()
    # slider_window = SliderWindow()
    # progress_bar_window = ProgressBarWindow()
    calendar_window = CalendarWindow()
    sys.exit(app.exec_())
