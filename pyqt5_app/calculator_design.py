# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_design_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 433)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setObjectName("widget")
        self.lbl_num1 = QtWidgets.QLabel(self.widget)
        self.lbl_num1.setGeometry(QtCore.QRect(40, 50, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lbl_num1.setFont(font)
        self.lbl_num1.setObjectName("lbl_num1")
        self.lbl_num2 = QtWidgets.QLabel(self.widget)
        self.lbl_num2.setGeometry(QtCore.QRect(40, 80, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.lbl_num2.setFont(font)
        self.lbl_num2.setObjectName("lbl_num2")
        self.txt_num1 = QtWidgets.QLineEdit(self.widget)
        self.txt_num1.setGeometry(QtCore.QRect(130, 41, 211, 31))
        self.txt_num1.setObjectName("txt_num1")
        self.txt_num2 = QtWidgets.QLineEdit(self.widget)
        self.txt_num2.setGeometry(QtCore.QRect(130, 80, 211, 31))
        self.txt_num2.setObjectName("txt_num2")
        self.btn_sum = QtWidgets.QPushButton(self.widget)
        self.btn_sum.setGeometry(QtCore.QRect(50, 130, 121, 61))
        self.btn_sum.setObjectName("btn_sum")
        self.btn_sub = QtWidgets.QPushButton(self.widget)
        self.btn_sub.setGeometry(QtCore.QRect(180, 130, 121, 61))
        self.btn_sub.setObjectName("btn_sub")
        self.btn_mult = QtWidgets.QPushButton(self.widget)
        self.btn_mult.setGeometry(QtCore.QRect(310, 130, 121, 61))
        self.btn_mult.setObjectName("btn_mult")
        self.btn_div = QtWidgets.QPushButton(self.widget)
        self.btn_div.setGeometry(QtCore.QRect(440, 130, 121, 61))
        self.btn_div.setObjectName("btn_div")
        self.lbl_result = QtWidgets.QLabel(self.widget)
        self.lbl_result.setGeometry(QtCore.QRect(150, 230, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        self.lbl_result.setFont(font)
        self.lbl_result.setLineWidth(1)
        self.lbl_result.setObjectName("lbl_result")
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 23))
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
        self.lbl_num1.setText(_translate("MainWindow", "Number 1:"))
        self.lbl_num2.setText(_translate("MainWindow", "Number 2:"))
        self.btn_sum.setText(_translate("MainWindow", "Summary"))
        self.btn_sub.setText(_translate("MainWindow", "Substraction"))
        self.btn_mult.setText(_translate("MainWindow", "Multiplication"))
        self.btn_div.setText(_translate("MainWindow", "Divide"))
        self.lbl_result.setText(_translate("MainWindow", "Result: "))
