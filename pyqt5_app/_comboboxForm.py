# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_combobox.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbCities = QtWidgets.QComboBox(self.centralwidget)
        self.cbCities.setGeometry(QtCore.QRect(80, 30, 271, 61))
        self.cbCities.setObjectName("cbCities")
        self.lblResult = QtWidgets.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(390, 30, 161, 51))
        self.lblResult.setObjectName("lblResult")
        self.btnGetItems = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetItems.setGeometry(QtCore.QRect(80, 200, 201, 81))
        self.btnGetItems.setObjectName("btnGetItems")
        self.btnLoadItems = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadItems.setGeometry(QtCore.QRect(350, 200, 211, 81))
        self.btnLoadItems.setObjectName("btnLoadItems")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(80, 310, 201, 81))
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblResult.setText(_translate("MainWindow", "TextLabel"))
        self.btnGetItems.setText(_translate("MainWindow", "Get Items"))
        self.btnLoadItems.setText(_translate("MainWindow", "Load Items"))
        self.btn_clear.setText(_translate("MainWindow", "Clear Items"))
