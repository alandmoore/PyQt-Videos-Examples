# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginbox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(254, 149)
        self.formLayout = QtWidgets.QFormLayout(LoginForm)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.username_input = QtWidgets.QLineEdit(LoginForm)
        self.username_input.setObjectName("username_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.username_input)
        self.label_2 = QtWidgets.QLabel(LoginForm)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_input = QtWidgets.QLineEdit(LoginForm)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_input)
        self.legalese_checkbox = QtWidgets.QCheckBox(LoginForm)
        self.legalese_checkbox.setObjectName("legalese_checkbox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.legalese_checkbox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_button = QtWidgets.QPushButton(LoginForm)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.login_button = QtWidgets.QPushButton(LoginForm)
        self.login_button.setObjectName("login_button")
        self.horizontalLayout.addWidget(self.login_button)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.label.setText(_translate("LoginForm", "Username"))
        self.label_2.setText(_translate("LoginForm", "Password"))
        self.legalese_checkbox.setText(_translate("LoginForm", "Agree to legalese"))
        self.cancel_button.setText(_translate("LoginForm", "Cancel"))
        self.login_button.setText(_translate("LoginForm", "Login"))
