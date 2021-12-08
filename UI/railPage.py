from ctypes import sizeof
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .Ui_files.Ui_railPage import Ui_railPage
from .auth import Auth
from . import APIs
import requests
import json

TOP = 1000
PTX_STATION_API = "https://ptx.transportdata.tw/MOTC/v3/Rail/TRA/Station?$top={}&$format=JSON".format(str(TOP))
PTX_TRAIN_LIVE_BOARD_API = "https://ptx.transportdata.tw/MOTC/v3/Rail/TRA/TrainLiveBoard?$top={}&$format=JSON".format(str(TOP))

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
        self.setFixedSize(self.size())

        self.stationArray = []  
        self.stationCrawler = StationCrawler()
        self.stationCrawler.finishSingal.connect(self.loadStationData)
        self.stationCrawler.start()

        self.TrainLiveBoardArray = []
        self.TrainLiveBoardCrawler = TrainLiveBoard_Crawler()
        self.TrainLiveBoardCrawler.finishSingal.connect(self.loadTrainLiveBoardData)
        self.TrainLiveBoardCrawler.start()

        self.backButton.clicked.connect(self.backHomePage)
        self.confirmButton.clicked.connect(self.loadTrainLiveBoardData)
        self.exchangeButton.clicked.connect(self.exchangeStation)

        # Style setting
        buttonStyle = "QPushButton {background-color:#FBAF00;border-radius:20px;}\
                        QPushButton:pressed{background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1 ,stop: 0 #007CBE, stop: 1 #007CBE)}"

    def loadStationData(self):
        JsonData = json.loads(self.stationCrawler.Data)
        self.stations = JsonData["Stations"]
        for index in range(len(self.stations)):
            self.stationArray.append(self.stations[index]["StationName"]["Zh_tw"])
        self.startComboBox.addItems(self.stationArray)
        self.endComboBox.addItems(self.stationArray)
        self.stationArray.clear()

    def loadTrainLiveBoardData(self):
        JsonData = json.loads(self.TrainLiveBoardCrawler.Data)
        self.TrainLiveBoard = JsonData["TrainLiveBoards"]
        for index in range(len(self.TrainLiveBoard)):
            info_format = self.TrainLiveBoard[index]["TrainNo"] + " , " + self.TrainLiveBoard[index]["TrainTypeName"]["Zh_tw"]
            self.TrainLiveBoardArray.append(info_format)
        self.stationList.addItems(self.TrainLiveBoardArray)
        self.TrainLiveBoardArray.clear()

    def backHomePage(self):
        self.close()
        self.homePage.show()


    def exchangeStation(self):
        temp = self.endComboBox.currentIndex()
        self.endComboBox.setCurrentIndex(self.startComboBox.currentIndex())
        self.startComboBox.setCurrentIndex(temp)



class StationCrawler(QThread):
    finishSingal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.API = PTX_STATION_API
        self.header = Auth(APIs.APP_ID,APIs.APP_KEY).getAuthHeader()
    
    def run(self):
        self.Data = requests.get(url=self.API,headers=self.header).text
        self.finishSingal.emit(1)

class TrainLiveBoard_Crawler(QThread):
    finishSingal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.API = PTX_TRAIN_LIVE_BOARD_API
        self.header = Auth(APIs.APP_ID,APIs.APP_KEY).getAuthHeader()
    
    def run(self):
        self.Data = requests.get(url=self.API,headers=self.header).text
        self.finishSingal.emit(1)