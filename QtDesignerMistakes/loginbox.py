# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginbox.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class authenticator():

    def __init__(self, auth_dict):

        self.auth_dict = auth_dict

    def authenticate(self, username, password, use_sso):
        if password and password == self.auth_dict.get(username):
            return True
        elif use_sso:
            return True
        else:
            return False

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(252, 149)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setObjectName("username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.use_sso = QtWidgets.QCheckBox(Form)
        self.use_sso.setObjectName("use_sso")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.use_sso)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.use_sso.stateChanged.connect(self.password.setDisabled)
        self.use_sso.stateChanged.connect(self.username.setDisabled)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Username"))
        self.label_2.setText(_translate("Form", "Password"))
        self.use_sso.setText(_translate("Form", "Use SSO login"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        self.pushButton.setText(_translate("Form", "Login"))

    def on_pushButton_clicked(self):
        auth = authenticator({'bob': 'pw', 'alice': 'secret'})
        username = self.username.text()
        password = self.password.text()
        use_sso = self.use_sso.isChecked()
        if auth.authenticate(username, password, use_sso):
            QtWidgets.QMessageBox.information(None, 'Success', 'You are in!')
            self.close()
        else:
            QtWidgets.QMessageBox.critical(None, 'Fail', 'Credentials not valid')
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    loginwindow = QtWidgets.QWidget()
    mygui = Ui_Form()
    mygui.setupUi(loginwindow)
    loginwindow.show()
    app.exec()

    
