# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.combSend = QtWidgets.QPushButton(Dialog)
        self.combSend.setGeometry(QtCore.QRect(290, 140, 89, 31))
        self.combSend.setObjectName("combSend")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 220, 67, 17))
        self.label.setObjectName("label")
        self.tokenSend = QtWidgets.QPushButton(Dialog)
        self.tokenSend.setGeometry(QtCore.QRect(290, 60, 89, 31))
        self.tokenSend.setObjectName("tokenSend")
        self.ID = QtWidgets.QTextEdit(Dialog)
        self.ID.setGeometry(QtCore.QRect(20, 60, 104, 31))
        self.ID.setObjectName("ID")
        self.Token = QtWidgets.QTextEdit(Dialog)
        self.Token.setGeometry(QtCore.QRect(160, 60, 104, 31))
        self.Token.setObjectName("Token")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 140, 241, 25))
        self.comboBox.setObjectName("comboBox")
        self.Response = QtWidgets.QLabel(Dialog)
        self.Response.setGeometry(QtCore.QRect(180, 220, 67, 17))
        self.Response.setText("")
        self.Response.setObjectName("Response")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 40, 67, 17))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.combSend.setText(_translate("Dialog", "Send"))
        self.label.setText(_translate("Dialog", "Response"))
        self.tokenSend.setText(_translate("Dialog", "Send"))
        self.label_2.setText(_translate("Dialog", "ID"))
        self.label_3.setText(_translate("Dialog", "Token"))

