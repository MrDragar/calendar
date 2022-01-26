# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newEvent.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_NewEvent(object):
    def setupUi(self, NewEvent):
        NewEvent.setObjectName("NewEvent")
        NewEvent.setFixedSize(800, 600)
        NewEvent.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(98, 160, 234), stop:1 rgb(153, 193, 241));\n"
"border: none;")
        self.centralwidget = QtWidgets.QWidget(NewEvent)
        self.centralwidget.setObjectName("centralwidget")
        self.timeEdit_start = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_start.setGeometry(QtCore.QRect(260, 300, 101, 40))
        self.timeEdit_start.setStyleSheet("background-color: white;\n"
"border: none;")
        self.timeEdit_start.setObjectName("timeEdit_start")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(340, 120, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("background-color: white;\n"
"border: none;")
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 210, 261, 61))
        self.label.setStyleSheet("background-color: white;\n"
"border: none;")
        self.label.setObjectName("label")
        self.timeEdit_end = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_end.setGeometry(QtCore.QRect(440, 300, 101, 40))
        self.timeEdit_end.setStyleSheet("background-color: white;\n"
"border: none;")
        self.timeEdit_end.setObjectName("timeEdit_end")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 210, 261, 61))
        self.label_2.setStyleSheet("background-color: white;\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 70, 241, 21))
        self.lineEdit.setStyleSheet("background-color: white;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 20, 231, 31))
        self.label_3.setStyleSheet("background-color: white;\n"
"")
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(260, 390, 291, 81))
        self.textEdit.setStyleSheet("background-color: white;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 350, 261, 21))
        self.label_4.setStyleSheet("background-color: white\n"
"")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 500, 141, 41))
        self.pushButton.setStyleSheet("background-color: white;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 510, 121, 31))
        self.pushButton_2.setStyleSheet("background-color: red\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        NewEvent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewEvent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        NewEvent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NewEvent)
        self.statusbar.setObjectName("statusbar")
        NewEvent.setStatusBar(self.statusbar)

        self.retranslateUi(NewEvent)
        QtCore.QMetaObject.connectSlotsByName(NewEvent)

    def retranslateUi(self, NewEvent):
        _translate = QtCore.QCoreApplication.translate
        NewEvent.setWindowTitle(_translate("NewEvent", "NewEvent"))
        self.label.setText(_translate("NewEvent", "Укажите время начала мероприятия"))
        self.label_2.setText(_translate("NewEvent", "Укажите время конца мероприятия"))
        self.label_3.setText(_translate("NewEvent", "Укажите название мероприятия"))
        self.label_4.setText(_translate("NewEvent", "TextLabel"))
        self.pushButton.setText(_translate("NewEvent", "Сохранить"))
        self.pushButton_2.setText(_translate("NewEvent", "Назад"))
