# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


# noinspection PyTypeChecker
class Ui_Calendar(object):
    def __init__ (self):
        self.months = [
            "Январь",
            "Февраль",
            "Март",
            "Апрель",
            "Май",
            "Июнь",
            "Июль",
            "Август",
            "Сентябрь",
            "Октябрь",
            "Ноябрь",
            "Декабрь",
        ]

    def setupUi (self, Calendar):
        Calendar.setObjectName("Calendar")
        Calendar.setEnabled(True)
        Calendar.setFixedSize(900, 700)
        Calendar.setStyleSheet("\n"
                               "background-color:qlineargradient"
                               "(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(98, 160, 234),"
                               " stop:1 rgb(153, 193, 241));\n"
                               "")
        self.centralwidget = QtWidgets.QWidget(Calendar)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 340, 791, 301))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_day_24 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_24.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_24.setObjectName("pushButton_day_24")
        self.gridLayout.addWidget(self.pushButton_day_24, 4, 3, 1, 1)
        self.pushButton_day_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_1.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                            "width: 100%;\n"
                                            "height: 100%;\n"
                                            "border: none;")
        self.pushButton_day_1.setObjectName("pushButton_day_1")
        self.gridLayout.addWidget(self.pushButton_day_1, 1, 1, 1, 1)
        self.pushButton_day_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_10.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_10.setObjectName("pushButton_day_10")
        self.gridLayout.addWidget(self.pushButton_day_10, 2, 3, 1, 1)
        self.pushButton_day_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_4.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                            "width: 100%;\n"
                                            "height: 100%;\n"
                                            "border: none;\n"
                                            "text-align: left;")
        self.pushButton_day_4.setObjectName("pushButton_day_4")
        self.gridLayout.addWidget(self.pushButton_day_4, 1, 4, 1, 1)
        self.pushButton_week_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_week_5.setEnabled(False)
        self.pushButton_week_5.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 6%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_week_5.setObjectName("pushButton_week_5")
        self.gridLayout.addWidget(self.pushButton_week_5, 5, 0, 1, 1)
        self.pushButton_day_32 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_32.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_32.setObjectName("pushButton_day_32")
        self.gridLayout.addWidget(self.pushButton_day_32, 5, 4, 1, 1)
        self.pushButton_mon = QtWidgets.QPushButton(self.widget)
        self.pushButton_mon.setEnabled(False)
        self.pushButton_mon.setStyleSheet("background-color: white;\n"
                                          "QPushBytton::unable{\n"
                                          "background-color: white;\n"
                                          "}")
        self.pushButton_mon.setObjectName("pushButton_mon")
        self.gridLayout.addWidget(self.pushButton_mon, 0, 1, 1, 1)
        self.pushButton_thue = QtWidgets.QPushButton(self.widget)
        self.pushButton_thue.setEnabled(False)
        self.pushButton_thue.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_thue.setObjectName("pushButton_thue")
        self.gridLayout.addWidget(self.pushButton_thue, 0, 2, 1, 1)
        self.pushButton_day_33 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_33.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_33.setObjectName("pushButton_day_33")
        self.gridLayout.addWidget(self.pushButton_day_33, 5, 5, 1, 1)
        self.pushButton_day_19 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_19.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_19.setObjectName("pushButton_day_19")
        self.gridLayout.addWidget(self.pushButton_day_19, 3, 5, 1, 1)
        self.pushButton_day_18 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_18.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_18.setObjectName("pushButton_day_18")
        self.gridLayout.addWidget(self.pushButton_day_18, 3, 4, 1, 1)
        self.pushButton_week_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_week_1.setEnabled(False)
        self.pushButton_week_1.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 6%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_week_1.setObjectName("pushButton_week_1")
        self.gridLayout.addWidget(self.pushButton_week_1, 1, 0, 1, 1)
        self.pushButton_day_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_6.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                            "width: 100%;\n"
                                            "height: 100%;\n"
                                            "border: none")
        self.pushButton_day_6.setObjectName("pushButton_day_6")
        self.gridLayout.addWidget(self.pushButton_day_6, 1, 6, 1, 1)
        self.pushButton_week_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_week_2.setEnabled(False)
        self.pushButton_week_2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 25%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_week_2.setObjectName("pushButton_week_2")
        self.gridLayout.addWidget(self.pushButton_week_2, 2, 0, 1, 1)
        self.pushButton_day_29 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_29.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_29.setObjectName("pushButton_day_29")
        self.gridLayout.addWidget(self.pushButton_day_29, 5, 1, 1, 1)
        self.pushButton_day_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                            "width: 100%;\n"
                                            "height: 100%;\n"
                                            "border: none")
        self.pushButton_day_2.setObjectName("pushButton_day_2")
        self.gridLayout.addWidget(self.pushButton_day_2, 1, 2, 1, 1)
        self.pushButton_day_20 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_20.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_20.setObjectName("pushButton_day_20")
        self.gridLayout.addWidget(self.pushButton_day_20, 3, 6, 1, 1)
        self.pushButton_day_13 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_13.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_13.setObjectName("pushButton_day_13")
        self.gridLayout.addWidget(self.pushButton_day_13, 2, 6, 1, 1)
        self.pushButton_day_23 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_23.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_23.setObjectName("pushButton_day_23")
        self.gridLayout.addWidget(self.pushButton_day_23, 4, 2, 1, 1)
        self.pushButton_day_21 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_21.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_21.setObjectName("pushButton_day_21")
        self.gridLayout.addWidget(self.pushButton_day_21, 3, 7, 1, 1)
        self.pushButton_day_22 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_22.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_22.setObjectName("pushButton_day_22")
        self.gridLayout.addWidget(self.pushButton_day_22, 4, 1, 1, 1)
        self.pushButton_day_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_5.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                            "width: 100%;\n"
                                            "height: 100%;\n"
                                            "border: none")
        self.pushButton_day_5.setObjectName("pushButton_day_5")
        self.gridLayout.addWidget(self.pushButton_day_5, 1, 5, 1, 1)
        self.pushButton_day_30 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_30.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_30.setObjectName("pushButton_day_30")
        self.gridLayout.addWidget(self.pushButton_day_30, 5, 2, 1, 1)
        self.pushButton_day_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_7.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                            "width: 100%;\n"
                                            "height: 100%;\n"
                                            "border: none;\n"
                                            "")
        self.pushButton_day_7.setObjectName("pushButton_day_7")
        self.gridLayout.addWidget(self.pushButton_day_7, 1, 7, 1, 1)
        self.pushButton_day_26 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_26.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_26.setObjectName("pushButton_day_26")
        self.gridLayout.addWidget(self.pushButton_day_26, 4, 5, 1, 1)
        self.pushButton_day_17 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_17.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_17.setObjectName("pushButton_day_17")
        self.gridLayout.addWidget(self.pushButton_day_17, 3, 3, 1, 1)
        self.pushButton_wedn = QtWidgets.QPushButton(self.widget)
        self.pushButton_wedn.setEnabled(False)
        self.pushButton_wedn.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_wedn.setObjectName("pushButton_wedn")
        self.gridLayout.addWidget(self.pushButton_wedn, 0, 3, 1, 1)
        self.pushButton_satu = QtWidgets.QPushButton(self.widget)
        self.pushButton_satu.setEnabled(False)
        self.pushButton_satu.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_satu.setObjectName("pushButton_satu")
        self.gridLayout.addWidget(self.pushButton_satu, 0, 6, 1, 1)
        self.pushButton_frid = QtWidgets.QPushButton(self.widget)
        self.pushButton_frid.setEnabled(False)
        self.pushButton_frid.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_frid.setObjectName("pushButton_frid")
        self.gridLayout.addWidget(self.pushButton_frid, 0, 5, 1, 1)
        self.pushButton_day_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_9.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                            "width: 100%;\n"
                                            "height: 100%;\n"
                                            "border: none")
        self.pushButton_day_9.setObjectName("pushButton_day_9")
        self.gridLayout.addWidget(self.pushButton_day_9, 2, 2, 1, 1)
        self.pushButton_day_12 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_12.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_12.setObjectName("pushButton_day_12")
        self.gridLayout.addWidget(self.pushButton_day_12, 2, 5, 1, 1)
        self.pushButton_week_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_week_4.setEnabled(False)
        self.pushButton_week_4.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 6%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_week_4.setObjectName("pushButton_week_4")
        self.gridLayout.addWidget(self.pushButton_week_4, 4, 0, 1, 1)
        self.pushButton_day_15 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_15.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_15.setObjectName("pushButton_day_15")
        self.gridLayout.addWidget(self.pushButton_day_15, 3, 1, 1, 1)
        self.pushButton_day_28 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_28.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_28.setObjectName("pushButton_day_28")
        self.gridLayout.addWidget(self.pushButton_day_28, 4, 7, 1, 1)
        self.pushButton_thur = QtWidgets.QPushButton(self.widget)
        self.pushButton_thur.setEnabled(False)
        self.pushButton_thur.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_thur.setObjectName("pushButton_thur")
        self.gridLayout.addWidget(self.pushButton_thur, 0, 4, 1, 1)
        self.pushButton_day_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_3.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                            "width: 100%;\n"
                                            "height: 100%;\n"
                                            "border: none")
        self.pushButton_day_3.setObjectName("pushButton_day_3")
        self.gridLayout.addWidget(self.pushButton_day_3, 1, 3, 1, 1)
        self.pushButton_sund = QtWidgets.QPushButton(self.widget)
        self.pushButton_sund.setEnabled(False)
        self.pushButton_sund.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pushButton_sund.setObjectName("pushButton_sund")
        self.gridLayout.addWidget(self.pushButton_sund, 0, 7, 1, 1)
        self.pushButton_day_27 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_27.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_27.setObjectName("pushButton_day_27")
        self.gridLayout.addWidget(self.pushButton_day_27, 4, 6, 1, 1)
        self.pushButton_day_16 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_16.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_16.setObjectName("pushButton_day_16")
        self.gridLayout.addWidget(self.pushButton_day_16, 3, 2, 1, 1)
        self.pushButton_day_25 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_25.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_25.setObjectName("pushButton_day_25")
        self.gridLayout.addWidget(self.pushButton_day_25, 4, 4, 1, 1)
        self.pushButton_day_11 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_11.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_11.setObjectName("pushButton_day_11")
        self.gridLayout.addWidget(self.pushButton_day_11, 2, 4, 1, 1)
        self.pushButton_day_14 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_14.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_14.setObjectName("pushButton_day_14")
        self.gridLayout.addWidget(self.pushButton_day_14, 2, 7, 1, 1)
        self.pushButton_day_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_8.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                            "width: 100%;\n"
                                            "height: 100%;\n"
                                            "border: none")
        self.pushButton_day_8.setObjectName("pushButton_day_8")
        self.gridLayout.addWidget(self.pushButton_day_8, 2, 1, 1, 1)
        self.pushButton_day_31 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_31.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_31.setObjectName("pushButton_day_31")
        self.gridLayout.addWidget(self.pushButton_day_31, 5, 3, 1, 1)
        self.pushButton_day_35 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_35.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_35.setObjectName("pushButton_day_35")
        self.gridLayout.addWidget(self.pushButton_day_35, 5, 7, 1, 1)
        self.pushButton_week_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_week_3.setEnabled(False)
        self.pushButton_week_3.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 6%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_week_3.setObjectName("pushButton_week_3")
        self.gridLayout.addWidget(self.pushButton_week_3, 3, 0, 1, 1)
        self.pushButton_day_34 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_34.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none")
        self.pushButton_day_34.setObjectName("pushButton_day_34")
        self.gridLayout.addWidget(self.pushButton_day_34, 5, 6, 1, 1)
        self.pushButton_day_36 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_36.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_day_36.setObjectName("pushButton_day_36")
        self.gridLayout.addWidget(self.pushButton_day_36, 6, 1, 1, 1)
        self.pushButton_day_37 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_37.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_day_37.setObjectName("pushButton_day_37")
        self.gridLayout.addWidget(self.pushButton_day_37, 6, 2, 1, 1)
        self.pushButton_day_38 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_38.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_day_38.setObjectName("pushButton_day_38")
        self.gridLayout.addWidget(self.pushButton_day_38, 6, 3, 1, 1)
        self.pushButton_day_39 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_39.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_day_39.setObjectName("pushButton_day_39")
        self.gridLayout.addWidget(self.pushButton_day_39, 6, 4, 1, 1)
        self.pushButton_day_40 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_40.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_day_40.setObjectName("pushButton_day_40")
        self.gridLayout.addWidget(self.pushButton_day_40, 6, 5, 1, 1)
        self.pushButton_day_41 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_41.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_day_41.setObjectName("pushButton_day_41")
        self.gridLayout.addWidget(self.pushButton_day_41, 6, 6, 1, 1)
        self.pushButton_day_42 = QtWidgets.QPushButton(self.widget)
        self.pushButton_day_42.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 100%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_day_42.setObjectName("pushButton_day_42")
        self.gridLayout.addWidget(self.pushButton_day_42, 6, 7, 1, 1)
        self.pushButton_week_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_week_6.setEnabled(False)
        self.pushButton_week_6.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                             "width: 6%;\n"
                                             "height: 100%;\n"
                                             "border: none;")
        self.pushButton_week_6.setObjectName("pushButton_week_6")
        self.gridLayout.addWidget(self.pushButton_week_6, 6, 0, 1, 1)
        self.label_month = QtWidgets.QLabel(self.centralwidget)
        self.label_month.setGeometry(QtCore.QRect(310, 220, 250, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.label_month.setFont(font)
        self.label_month.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                       "border: none;\n"
                                       "text-align: сenter;")
        self.label_month.setObjectName("label_moun")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(90, 230, 121, 51))
        self.pushButton_back.setStyleSheet("background-color: white;")
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_forw = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_forw.setGeometry(QtCore.QRect(660, 230, 121, 51))
        self.pushButton_forw.setStyleSheet("background-color: white;")
        self.pushButton_forw.setObjectName("pushButton_forw")
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        self.label_year.setGeometry(QtCore.QRect(330, 150, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.label_year.setFont(font)
        self.label_year.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                      "border: none;\n"
                                      "text-align: сenter;")
        self.label_year.setObjectName("label_year")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(760, 10, 111, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("background-color: white;\n"
                                      "")
        self.label_time.setObjectName("label_time")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 30, 256, 192))
        self.textBrowser.setStyleSheet("background-color: white;")
        self.textBrowser.setObjectName("textBrowser")
        self.label_task = QtWidgets.QLabel(self.centralwidget)
        self.label_task.setGeometry(QtCore.QRect(20, 0, 141, 21))
        self.label_task.setStyleSheet("background-color: white;")
        self.label_task.setObjectName("label_task")
        Calendar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calendar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
        self.menubar.setObjectName("menubar")
        Calendar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calendar)
        self.statusbar.setObjectName("statusbar")
        Calendar.setStatusBar(self.statusbar)

        self.retranslateUi(Calendar)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi (self, Calendar):
        _translate = QtCore.QCoreApplication.translate
        Calendar.setWindowTitle(_translate("Calendar", "Calendar"))
        self.pushButton_day_24.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_1.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_10.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_4.setText(_translate("Calendar", "PushButton"))
        self.pushButton_week_5.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_32.setText(_translate("Calendar", "PushButton"))
        self.pushButton_mon.setText(_translate("Calendar", "Пн"))
        self.pushButton_thue.setText(_translate("Calendar", "Вт"))
        self.pushButton_day_33.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_19.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_18.setText(_translate("Calendar", "PushButton"))
        self.pushButton_week_1.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_6.setText(_translate("Calendar", "PushButton"))
        self.pushButton_week_2.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_29.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_2.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_20.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_13.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_23.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_21.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_22.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_5.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_30.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_7.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_26.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_17.setText(_translate("Calendar", "PushButton"))
        self.pushButton_wedn.setText(_translate("Calendar", "Ср"))
        self.pushButton_satu.setText(_translate("Calendar", "Сб"))
        self.pushButton_frid.setText(_translate("Calendar", "Пт"))
        self.pushButton_day_9.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_12.setText(_translate("Calendar", "PushButton"))
        self.pushButton_week_4.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_15.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_28.setText(_translate("Calendar", "PushButton"))
        self.pushButton_thur.setText(_translate("Calendar", "Чт"))
        self.pushButton_day_3.setText(_translate("Calendar", "PushButton"))
        self.pushButton_sund.setText(_translate("Calendar", "Вс"))
        self.pushButton_day_27.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_16.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_25.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_11.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_14.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_8.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_31.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_35.setText(_translate("Calendar", "PushButton"))
        self.pushButton_week_3.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_34.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_36.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_37.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_38.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_39.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_40.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_41.setText(_translate("Calendar", "PushButton"))
        self.pushButton_day_42.setText(_translate("Calendar", "PushButton"))
        self.pushButton_week_6.setText(_translate("Calendar", "PushButton"))
        self.label_month.setText(_translate("Calendar", "Май"))
        self.pushButton_back.setText(_translate("Calendar", "Назад"))
        self.pushButton_forw.setText(_translate("Calendar", "Вперёд"))
        self.label_year.setText(_translate("Calendar", "2021"))
        self.label_time.setText(_translate("Calendar", "10:22:10"))
        self.label_task.setText(_translate("Calendar", "Ближайшие задачи"))
        self.set_dicts()

    def set_dicts (self):
        self.days_buttons = [
            self.pushButton_day_1,
            self.pushButton_day_2,
            self.pushButton_day_3,
            self.pushButton_day_4,
            self.pushButton_day_5,
            self.pushButton_day_6,
            self.pushButton_day_7,
            self.pushButton_day_8,
            self.pushButton_day_9,
            self.pushButton_day_10,
            self.pushButton_day_11,
            self.pushButton_day_12,
            self.pushButton_day_13,
            self.pushButton_day_14,
            self.pushButton_day_15,
            self.pushButton_day_16,
            self.pushButton_day_17,
            self.pushButton_day_18,
            self.pushButton_day_19,
            self.pushButton_day_20,
            self.pushButton_day_21,
            self.pushButton_day_22,
            self.pushButton_day_23,
            self.pushButton_day_24,
            self.pushButton_day_25,
            self.pushButton_day_26,
            self.pushButton_day_27,
            self.pushButton_day_28,
            self.pushButton_day_29,
            self.pushButton_day_30,
            self.pushButton_day_31,
            self.pushButton_day_32,
            self.pushButton_day_33,
            self.pushButton_day_34,
            self.pushButton_day_35,
            self.pushButton_day_36,
            self.pushButton_day_37,
            self.pushButton_day_38,
            self.pushButton_day_39,
            self.pushButton_day_40,
            self.pushButton_day_41,
            self.pushButton_day_42,
        ]
        self.weeks = [
            self.pushButton_week_1,
            self.pushButton_week_2,
            self.pushButton_week_3,
            self.pushButton_week_4,
            self.pushButton_week_5,
            self.pushButton_week_6
        ]

    def set_data (self, year, month, first_week, first_wday, day_count, day, current_data):
        self.label_year.setText(str(year))
        self.label_month.setText(self.months[month])
        for i in self.days_buttons:
            i.setStyleSheet("background: white; width: 100%; height: 100%; border: none")
            i.setText("")
        for i in range(0, day_count + 1):
            self.days_buttons[i + first_wday].setText(str(i + 1))
            if i + 1 == day:
                if current_data:
                    self.days_buttons[i + first_wday].setStyleSheet("background: red; width: 100%; height: 100%;"
                                                                    "border: none")
                else:
                    self.days_buttons[i + first_wday].setStyleSheet("background: coral; width: 100%; height: 100%;"
                                                                    "border: none")

        for i in range(6):
            self.weeks[i].setText(str(i + first_week))
