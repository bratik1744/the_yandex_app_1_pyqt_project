# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homework_information_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label_name_inf = QtWidgets.QLabel(Form)
        self.label_name_inf.setGeometry(QtCore.QRect(150, 10, 241, 16))
        self.label_name_inf.setObjectName("label_name_inf")
        self.label_virtual_coins_inf = QtWidgets.QLabel(Form)
        self.label_virtual_coins_inf.setGeometry(QtCore.QRect(150, 70, 241, 16))
        self.label_virtual_coins_inf.setObjectName("label_virtual_coins_inf")
        self.label_virtual_coins = QtWidgets.QLabel(Form)
        self.label_virtual_coins.setGeometry(QtCore.QRect(10, 70, 131, 16))
        self.label_virtual_coins.setObjectName("label_virtual_coins")
        self.label_exp = QtWidgets.QLabel(Form)
        self.label_exp.setGeometry(QtCore.QRect(10, 50, 55, 16))
        self.label_exp.setObjectName("label_exp")
        self.label_name = QtWidgets.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.label_name.setObjectName("label_name")
        self.label_lesson = QtWidgets.QLabel(Form)
        self.label_lesson.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_lesson.setObjectName("label_lesson")
        self.label_term_inf = QtWidgets.QLabel(Form)
        self.label_term_inf.setGeometry(QtCore.QRect(150, 30, 241, 16))
        self.label_term_inf.setObjectName("label_term_inf")
        self.label_term = QtWidgets.QLabel(Form)
        self.label_term.setGeometry(QtCore.QRect(10, 30, 55, 16))
        self.label_term.setObjectName("label_term")
        self.label_lesson_inf = QtWidgets.QLabel(Form)
        self.label_lesson_inf.setGeometry(QtCore.QRect(150, 90, 241, 16))
        self.label_lesson_inf.setObjectName("label_lesson_inf")
        self.label_exp_inf = QtWidgets.QLabel(Form)
        self.label_exp_inf.setGeometry(QtCore.QRect(150, 50, 241, 16))
        self.label_exp_inf.setObjectName("label_exp_inf")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 230, 401, 71))
        self.pushButton.setObjectName("pushButton")
        self.label_task = QtWidgets.QLabel(Form)
        self.label_task.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_task.setObjectName("label_task")
        self.label_described_inf_2 = QtWidgets.QLabel(Form)
        self.label_described_inf_2.setGeometry(QtCore.QRect(150, 110, 241, 16))
        self.label_described_inf_2.setObjectName("label_described_inf_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_name_inf.setText(_translate("Form", "s"))
        self.label_virtual_coins_inf.setText(_translate("Form", "s"))
        self.label_virtual_coins.setText(_translate("Form", "Виртуальные монеты"))
        self.label_exp.setText(_translate("Form", "Опыт:"))
        self.label_name.setText(_translate("Form", "Имя:"))
        self.label_lesson.setText(_translate("Form", "Урок:"))
        self.label_term_inf.setText(_translate("Form", "s"))
        self.label_term.setText(_translate("Form", "Срок:"))
        self.label_lesson_inf.setText(_translate("Form", "s"))
        self.label_exp_inf.setText(_translate("Form", "s"))
        self.pushButton.setText(_translate("Form", "Назад"))
        self.label_task.setText(_translate("Form", "Задача:"))
        self.label_described_inf_2.setText(_translate("Form", "s"))
