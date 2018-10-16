#！、usr/bin/python3
# -*- coding:utf-8 -*-

"""
A simple PyQt Window contains a Menubar which contains 
many menu(a menu even contains a submenu), Toolbar, Statusbar 
and TextEdit

Author: simperful
Date: 2018-10-16
Reference: http://zetcode.com/gui/pyqt5/menustoolbars/
"""

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, 
QAction, qApp, QMenu, QTextEdit)
from PyQt5.QtGui import QIcon


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        ########################################################
        # define a menubar, it contains two menu: File and View
        #########################################################
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        viewMenu = menubar.addMenu('View')

        ##### File Menu ##########################
        # exit action
        exitAct = QAction(QIcon("../image/exit.png"), "&Exit", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit application")
        exitAct.triggered.connect(qApp.quit)

        # import menu contains a submenu Import Mail(an Action)
        impmenu = QMenu('Import', self)
        impAct = QAction('Import Mail', self)
        impmenu.addAction(impAct)

        newAct = QAction('New', self) # do nothing,just a menu(an action)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impmenu) 
        fileMenu.addAction(exitAct)

        ######## View Menu #############################
        # view statusbar action
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        ##################################################
        # status bar         
        ##################################################
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        ###################################################
        # define a toolbar
        ###################################################
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        ####################################################
        # A textedit
        ####################################################
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        #####################################################
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Statusbar')
        self.show()

    # I will learn it in the next few chapters
    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    my_window = MyWindow()
    sys.exit(app.exec_())