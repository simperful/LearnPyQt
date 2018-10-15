#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
In this examle, I create a simple window in PyQt5.

Date：2018-10-15 
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, 
QPushButton, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QIcon, QFont

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.setToolTip('This is a <b>QPushButton</b> widget')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 100)

        self.resize(300, 220)
        self.center()
        self.setWindowTitle('My First PyQt Window')
        self.setWindowIcon(QIcon("../image/icon.png"))

        self.show()


    def closeEvent(self, event):  # if you use the 'Exit' button, this won't be called

        reply = QMessageBox.question(self, 'Message', 
        "Are you sure to quit?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    
    def center(self):

        qr = self.frameGeometry() # get a rectangle specifying the geometry of the main window
        cp = QDesktopWidget().availableGeometry().center() # figure out the screen resolution of our monitor, and get the center point
        qr.moveCenter(cp) #  set the center of the rectangle to the center of the screen
        self.move(qr.topLeft()) # move the top-left point of the application window to the top-left point of the qr rectangle, thus centering the window on our screen. 



if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyWindow()
    sys.exit(app.exec_())