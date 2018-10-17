# ！/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication,
QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QTextEdit, QLineEdit)


# The following example using absolute position
# class Example(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.initUI()

    
#     def initUI(self):

#         lbl1 = QLabel('simperful', self)
#         lbl1.move(15, 10)

#         lbl2 = QLabel('practice', self)
#         lbl2.move(35, 40)

#         lbl3 = QLabel('for myself', self)
#         lbl3.move(55, 70)

#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("Absolute Position")
#         self.show()


class UseLayout(QWidget):
# This class is a example using QHBoxLayout and QVBoxLayout

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        # The stretch adds a stretchable space 
        # before the two buttons. 
        # This will push them to the right of the window. ——according to the tutorial
        # when I change 1 to another number(2 or 30), nothing has changed
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        # This will push them to the bottom of the window. —— I guess before the I read the tutorial
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Use layout")
        self.show()



class CalculatorUI(QWidget):
# This class is an example using QGridLayout

    def __init__(self):

        super().__init__()
        
        self.initUI()


    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()



class ReviewEdit(QWidget):
# This is class using widgets that can span multiple columns or grows 
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        title_lable = QLabel('Title')
        author_lable = QLabel('Author')
        review_lable = QLabel('Review')

        title_edit = QLineEdit()
        author_edit = QLineEdit()
        review_edit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title_lable, 1, 0)
        grid.addWidget(title_edit, 1, 1)

        grid.addWidget(author_lable, 2, 0)
        grid.addWidget(author_edit, 2, 1)

        grid.addWidget(review_lable, 3, 0)
        grid.addWidget(review_edit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # ex = UseLayout()
    #calculator = CalculatorUI()
    review_window = ReviewEdit()
    sys.exit(app.exec_())