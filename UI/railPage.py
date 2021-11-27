from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .Ui_files.Ui_railPage import Ui_railPage

import requests
import json

TOP = 500
PTX_STATION_API = "https://ptx.transportdata.tw/MOTC/v3/Rail/TRA/Station?$top={}&$format=JSON".format(str(TOP))

class RailPage(QDialog,Ui_railPage):
    """
    RailPage
    """
    def __init__(self,homePage):
        super(RailPage,self).__init__()
        self.homePage = homePage
        self.setupUi(self)
        self.show()
        self.setWindowTitle("Railway")
        self.setWindowIcon(QIcon("./UI/images/railPage_icon.png"))
        self.setStyleSheet("background-color:#F8FFE5")

        self.stationArray = []
        self.stationData = stationCrawler()
        self.stationData.finishSingal.connect(self.loadData)
        self.stationData.start()

        self.backButton.clicked.connect(self.backHomePage)
        self.confirmButton.clicked.connect(self.loadData)
        self.exchangeButton.clicked.connect(self.exchangeStation)

        # Style setting
        buttonStyle = "QPushButton {background-color:#FBAF00;border-radius:20px;}\
                        QPushButton:pressed{background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 ,stop: 0 #007CBE, stop: 1 #007CBE)}"

    def loadData(self):
        self.jsonData = json.loads(self.stationData.Data)
        self.jsonStation = self.jsonData["Stations"]
        for index in range(len(self.jsonStation)):
            self.stationArray.append(self.jsonStation[index]["StationName"]["Zh_tw"])
        self.startComboBox.clear()
        self.endComboBox.clear()
        self.startComboBox.addItems(self.stationArray)
        self.endComboBox.addItems(self.stationArray)

    def backHomePage(self):
        self.close()
        self.homePage.show()


    def exchangeStation(self):
        temp = self.endComboBox.currentIndex()
        self.endComboBox.setCurrentIndex(self.startComboBox.currentIndex())
        self.startComboBox.setCurrentIndex(temp)

class stationCrawler(QThread):
    finishSingal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.API = PTX_STATION_API
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',}
    
    def run(self):
        self.Data = requests.get(url=self.API,headers=self.header,json=True).text
        self.finishSingal.emit(1)