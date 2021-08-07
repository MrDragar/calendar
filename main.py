import sys
import time
import json
from calendar import Ui_Calendar
from newEvent import Ui_NewEvent
from PyQt5 import QtWidgets
import time as tm
import datetime
from PyQt5.QtCore import QThread
import os
from functools import partial

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Calendar()
ui.setupUi(MainWindow)
MainWindow.show()
if sys.platform == "linux" or "linux2":
    task_dir = os.path.join(os.path.join(os.environ['HOME']), 'calendar')
else:
    task_dir = os.path.join(os.path.join(os.environ['HOME']), 'calendar')
name_file_task = 'tasks.json'
if os.path.exists(task_dir):
    pass
else:
    os.mkdir(task_dir)
f = open(name_file_task, "w", encoding="utf-8")
f.close()


class functions():
    def __init__(self):
        self.time = tm.localtime()
        self.m_plus = 0
        self.name_file_task = os.path.join(task_dir, name_file_task)
    # time = tm.localtime()
    months = {
        '1': "Январь",
        '2': "Февраль",
        '3': "Март",
        '4': "Апрель",
        '5': "Май",
        '6': "Июнь",
        '7': "Июль",
        '8': "Август",
        '9': "Сентябрь",
        '10': "Октябрь",
        '11': "Ноябрь",
        '12': "Декабрь",
    }
    days = {
        '1': ui.pushButton_day_1,
        '2': ui.pushButton_day_2,
        '3': ui.pushButton_day_3,
        '4': ui.pushButton_day_4,
        '5': ui.pushButton_day_5,
        '6': ui.pushButton_day_6,
        '7': ui.pushButton_day_7,
        '8': ui.pushButton_day_8,
        '9': ui.pushButton_day_9,
        '10': ui.pushButton_day_10,
        '11': ui.pushButton_day_11,
        '12': ui.pushButton_day_12,
        '13': ui.pushButton_day_13,
        '14': ui.pushButton_day_14,
        '15': ui.pushButton_day_15,
        '16': ui.pushButton_day_16,
        '17': ui.pushButton_day_17,
        '18': ui.pushButton_day_18,
        '19': ui.pushButton_day_19,
        '20': ui.pushButton_day_20,
        '21': ui.pushButton_day_21,
        '22': ui.pushButton_day_22,
        '23': ui.pushButton_day_23,
        '24': ui.pushButton_day_24,
        '25': ui.pushButton_day_25,
        '26': ui.pushButton_day_26,
        '27': ui.pushButton_day_27,
        '28': ui.pushButton_day_28,
        '29': ui.pushButton_day_29,
        '30': ui.pushButton_day_30,
        '31': ui.pushButton_day_31,
        '32': ui.pushButton_day_32,
        '33': ui.pushButton_day_33,
        '34': ui.pushButton_day_34,
        '35': ui.pushButton_day_35,
        '36': ui.pushButton_day_36,
        '37': ui.pushButton_day_37,
        '38': ui.pushButton_day_38,
        '39': ui.pushButton_day_39,
        '40': ui.pushButton_day_40,
        '41': ui.pushButton_day_41,
        '42': ui.pushButton_day_42,
    }
    weeks={
        '1': ui.pushButton_week_1,
        '2': ui.pushButton_week_2,
        '3': ui.pushButton_week_3,
        '4': ui.pushButton_week_4,
        '5': ui.pushButton_week_5,
        '6': ui.pushButton_week_6
    }
    def setup_edit(self):
        self.selected_moun = (self.time.tm_mon - 1 + self.m_plus)
        self.selected_year = self.selected_moun // 12 + self.time.tm_year
        ui.label_moun.setText(self.months[str(self.selected_moun % 12 + 1)])
        ui.label_year.setText(str(self.selected_year))
        self.first_wday = datetime.datetime(self.selected_year, self.selected_moun % 12 + 1, 1).isoweekday()
        self.first_wday_year = datetime.datetime(self.selected_year, 1, 1).isoweekday()
        self.days_year = 1
        for u in range(self.selected_moun % 12+1):
            for i in range(32):
                try:
                    a = datetime.date(self.selected_year, u, i + 1)

                except:
                    break
                self.days_year += 1
        print(self.days_year)
        print(self.first_wday_year)
        self.week_year = (self.days_year + self.first_wday_year - 1) // 7 + 1
        for i in range(1, 7):
            self.weeks[str(i)].setText(str(self.week_year+i-1))

        self.last_day = 0
        for i in range(32):
            try:
                a = datetime.date(self.selected_year, self.selected_moun % 12 + 1, i + 1)
            except:
                break
            self.days[str(i + self.first_wday)].setText(str(i + 1))
            self.last_day += 1
            if self.time.tm_mon == self.selected_moun + 1 and i == self.time.tm_mday - 1:
                self.days[str(i + self.first_wday)].setStyleSheet(("background-color:red;\n"
"width: 100%;\n"
"height: 100%;\n"
"border: none"))
            else:
                self.days[str(i + self.first_wday)].setStyleSheet(("background-color:rgb(255, 255, 255);\n"
"width: 100%;\n"
"height: 100%;\n"
"border: none"))
        self.last_day += 1
        for i in range(self.last_day + self.first_wday - 1, 43):
            self.days[str(i)].setText('')
        for i in range(1, self.first_wday):
            self.days[str(i)].setText('')

    def edit_time(self):
        self.time = tm.localtime()
        hour = str(self.time.tm_hour)
        min = str(self.time.tm_min)
        sec = str(self.time.tm_sec)
        if int(hour) < 10 : hour = "0" + hour
        if int(min) < 10: min = "0" + min
        if int(sec) < 10 : sec = "0" + sec
        ui.label_time.setText(hour + ":" + min + ':' + sec)
        if hour == "00" and min == "00" and (sec == "00" or "01" or "02" or "03"):
            self.setup_edit()


    def open_writing(self, day):
        print(day)
        writing_wind = QtWidgets.QMainWindow()
        ui2 = Ui_NewEvent()
        ui2.setupUi(writing_wind)
        writing_wind.show()
        ui2.dateEdit.close()
        MainWindow.close()
        def create_task():
            from pathlib import Path
            path = Path(self.name_file_task)


            try:
                data = json.loads(path.read_text(encoding='utf-8'))
                print(data.keys(), "dasd")
                b = 0
                for i in (data.keys()):
                    b+= 1

                data[str(b+1)]=({"day":day, "name": ui2.lineEdit.text(), "time_start": ui2.timeEdit_start.text(), "time_end": ui2.timeEdit_end.text(),
                        "text":ui2.lineEdit.text()})
            except:
                f = open(self.name_file_task, "w", encoding="utf-8")
                f.close()

                data ={}
                data['1'] = {"day":day, "name": ui2.lineEdit.text(), "time_start": ui2.timeEdit_start.text(), "time_end": ui2.timeEdit_end.text(),
                        "text":ui2.lineEdit.text()}
            path.write_text(json.dumps(data), encoding='utf-8')
            exiting()
        def exiting():
            writing_wind.close()
            MainWindow.show()
        ui2.pushButton.clicked.connect(create_task)
        ui2.pushButton_2.clicked.connect(exiting)

    def edit_m_plus(self):
        self.m_plus += 1
        self.setup_edit()

    def edit_m_min(self):
        self.m_plus -= 1
        self.setup_edit()

    def reading(self):
        from pathlib import Path
        path = Path(self.name_file_task)

        try:
            data = json.loads(path.read_text(encoding='utf-8'))
            keys = data.keys()
            a = []
            print(data)
            ui.textBrowser.setText(data['1']['time_start'])
            # for i in data:
            #     a.append('дата '+ )

        except: pass







function = functions()
function.setup_edit()
function.edit_time()
function.reading()

class eding_time(QThread):
    def __init__(self, function, parents=None):
        super(eding_time, self).__init__(parents)
        self.a = function
    def run(self):
        while True:
            time.sleep(1)
            self.a.edit_time()


ui.pushButton_forw.clicked.connect(function.edit_m_plus)
ui.pushButton_back.clicked.connect(function.edit_m_min)


for i in range(42):
    a = (function.days[str(i+1)].text())
    if a != '':
        function.days[str(i+1)].clicked.connect(partial(function.open_writing, a))

class tasks:
    pass

ui.eding1_time = eding_time(function=function)
ui.eding1_time.start()
sys.exit(app.exec_())
