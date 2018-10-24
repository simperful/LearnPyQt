#！/usr/bin/python3
# -*- coding:utf-8 -*-

"""
In this dialog, we receive data from a QInputDialog dialog
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
    QInputDialog, QApplication, QFrame, QColorDialog, QGridLayout,
    QSizePolicy, QFontDialog, QLabel, QMainWindow, QTextEdit, QAction,
    QFileDialog)
from PyQt5.QtGui import QColor, QIcon
import sys

class DialogWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog')
        # self.btn.move(20, 20)
        self.btn.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit()

        self.frm = QFrame()
        self.frm.setStyleSheet("QWidget {background-color: %s}"%col.name())
        self.frm.setFixedSize(200, 100)

        self.lbl = QLabel('Knowledge only matters')

        grid.addWidget(self.btn, 1, 0)
        grid.addWidget(self.le, 1, 1)
        grid.addWidget(self.lbl, 2, 0)
        grid.addWidget(self.frm)
        self.setLayout(grid)

        self.setGeometry(300, 300, 290, 180)
        self.setWindowTitle("Dialog")
        self.show()


    def showDialog(self):

        text, ok = QInputDialog.getText(self, 
            'Input Dialog', 'Ennter your name:')
        #  The first string is a dialog title, 
        # the second one is a message within the dialog.
        if ok:
            self.le.setText(str(text))
        else:
            col = QColorDialog.getColor()

            if col.isValid():
                self.frm.setStyleSheet("QWidget {background-color: %s}"
                    %col.name())
            else:
                font, ok = QFontDialog.getFont()
                if ok:
                    self.lbl.setFont(font)



class FileWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        self.statusBar()

        open_file = QAction(QIcon("../image/open.png"), 'Open', self)
        open_file.setShortcut("Ctrl+O")
        open_file.setStatusTip('Open new file')
        open_file.triggered.connect(self.showDialog)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(open_file)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("File Dialog")
        self.show()


    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.text_edit.setText(data)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    # dialog_window = DialogWindow()
    file_window = FileWindow()
    sys.exit(app.exec_())