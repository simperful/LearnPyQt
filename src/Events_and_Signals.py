#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
In this example, we connect a signal of a QSlider to a slot of a QLCDNumber
"""

import sys
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout,
QApplication, QGridLayout, QLabel, QPushButton, QMainWindow)

class Event_Slots(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    
    def initUI(self):

        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        
        self.status_lable = QLabel("Status: No button is pressed", self)

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0}, y: {1}".format(x, y)

        self.lable = QLabel(self.text, self)

        grid.addWidget(self.lable, 1, 0)
        grid.addWidget(lcd, 2, 0)
        grid.addWidget(sld, 3, 0)
        grid.addWidget(self.status_lable, 4, 0)
        grid.addWidget(btn1, 5, 0)
        grid.addWidget(btn2, 5, 1)

        self.setMouseTracking(True) 
        # Mouse tracking is disabled by default, only when the mouse button is pressed
        # the mouseMoveEvent can track the mouse.
        # if we enable it, we can track the mouse without press any mouse button
        # and if we press the mouse button, the event handler can also track the mouse

        self.setLayout(grid)

        sld.valueChanged.connect(lcd.display)
        # connect a valueChanged signal of the slider 
        # to the display slot of the lcd number

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Signal and slot')
        self.show()


    def keyPressEvent(self, e):
    # reimplement the keyPressEvent() event handler
        if e.key() == Qt.Key_Escape:
            self.close()


    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x: {0}, y: {1}".format(x, y)
        self.lable.setText(text)


    def buttonClicked(self):

        sender = self.sender()
        self.status_lable.setText("Status:" + sender.text() + " was pressed")



class Communicate(QObject):

    closeApp = pyqtSignal()




class EmitSignals(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.c = Communicate()
        self.c.closeApp.connect(self.close) # close() slot of the QMainWindow.
        # connect is the attribute of the QObject

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Signal and slot')
        self.show()


    def mousePressEvent(self, event):

        self.c.closeApp.emit()



if __name__ == "__main__":

    app = QApplication(sys.argv)
    # event_slots = Event_Slots()
    emit_signal = EmitSignals()
    sys.exit(app.exec_())