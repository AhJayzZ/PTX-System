# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\AhJayzZ\Desktop\NTUST\Project\SideProject\PTX System\UI\Ui_files\homePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homePage(object):
    def setupUi(self, homePage):
        homePage.setObjectName("homePage")
        homePage.resize(1009, 355)
        self.gridLayout = QtWidgets.QGridLayout(homePage)
        self.gridLayout.setObjectName("gridLayout")
        self.titleLabel = QtWidgets.QLabel(homePage)
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.showLabel = QtWidgets.QLabel(homePage)
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.showLabel.setFont(font)
        self.showLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.showLabel.setObjectName("showLabel")
        self.gridLayout.addWidget(self.showLabel, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.railButton = QtWidgets.QPushButton(homePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.railButton.sizePolicy().hasHeightForWidth())
        self.railButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.railButton.setFont(font)
        self.railButton.setObjectName("railButton")
        self.horizontalLayout.addWidget(self.railButton)
        self.highSpeedRailButton = QtWidgets.QPushButton(homePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.highSpeedRailButton.sizePolicy().hasHeightForWidth())
        self.highSpeedRailButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.highSpeedRailButton.setFont(font)
        self.highSpeedRailButton.setObjectName("highSpeedRailButton")
        self.horizontalLayout.addWidget(self.highSpeedRailButton)
        self.busButton = QtWidgets.QPushButton(homePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.busButton.sizePolicy().hasHeightForWidth())
        self.busButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.busButton.setFont(font)
        self.busButton.setObjectName("busButton")
        self.horizontalLayout.addWidget(self.busButton)
        self.airplaneButton = QtWidgets.QPushButton(homePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.airplaneButton.sizePolicy().hasHeightForWidth())
        self.airplaneButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.airplaneButton.setFont(font)
        self.airplaneButton.setObjectName("airplaneButton")
        self.horizontalLayout.addWidget(self.airplaneButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.retranslateUi(homePage)
        QtCore.QMetaObject.connectSlotsByName(homePage)

    def retranslateUi(self, homePage):
        _translate = QtCore.QCoreApplication.translate
        homePage.setWindowTitle(_translate("homePage", "Dialog"))
        self.titleLabel.setText(_translate("homePage", "公眾交通運輸查詢系統 PTX System"))
        self.showLabel.setText(_translate("homePage", "我想查詢..."))
        self.railButton.setText(_translate("homePage", "台鐵"))
        self.highSpeedRailButton.setText(_translate("homePage", "高鐵"))
        self.busButton.setText(_translate("homePage", "公車"))
        self.airplaneButton.setText(_translate("homePage", "飛機"))