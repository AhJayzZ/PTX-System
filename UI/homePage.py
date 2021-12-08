from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .Ui_files.Ui_homePage import Ui_homePage
from .railPage import RailPage

class HomePage(QDialog,Ui_homePage):
    """
    LoginPage
    """
    def __init__(self):
        super(HomePage,self).__init__()
        self.setupUi(self)
        self.show()
        self.setWindowTitle("Home")
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon("./UI/images/homePage_icon.png"))
        self.setStyleSheet("background-color:#1B9AAA")


        self.railButton.clicked.connect(self.openRailPage)


        # Style setting
        buttonStyle = "QPushButton {background-color:#FBAF00;border-radius:20px;}\
                        QPushButton:pressed{background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 ,stop: 0 #007CBE, stop: 1 #007CBE)}"
        self.railButton.setStyleSheet(buttonStyle)
        self.highSpeedRailButton.setStyleSheet(buttonStyle)
        self.busButton.setStyleSheet(buttonStyle)
        self.airplaneButton.setStyleSheet(buttonStyle)

    def openRailPage(self):
        self.hide()
        self.railPage = RailPage(self)