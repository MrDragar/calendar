from PySide2 import QtWidgets
from view.calendar_window import Ui_Calendar
from view.NewEvent_window import Ui_NewEvent
from model.calendar_model import CalendarModel


class Presenter(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(Presenter, self).__init__(sys_argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.MainUI = Ui_Calendar()
        self.calendar_model = CalendarModel()
        self.NewEventUI = Ui_NewEvent()
        self.open_new_event_window()
        self.open_main_window()
        self.MainWindow.show()

    def open_main_window(self):
        self.MainUI.setupUi(self.MainWindow)
        self.MainUI.pushButton_forw.clicked.connect(self.go_forward)
        self.set_data()

    def set_data(self):
        self.MainUI.set_data(self.calendar_model.year, self.calendar_model.month, self.calendar_model.first_week,
                             self.calendar_model.first_wday, self.calendar_model.days_count, self.calendar_model.day,
                             self.calendar_model.current_data)

    def open_new_event_window(self):
        self.NewEventUI.setupUi(self.MainWindow)
        self.NewEventUI.pushButton_2.clicked.connect(self.open_main_window)

    def go_forward(self):
        self.calendar_model.plus_month()
        print(1)
        self.set_data()
        pass

    pass
