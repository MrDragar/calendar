import time
import datetime
from calendar import monthrange


class CalendarModel:
    def __init__(self):
        self.localtime = time.localtime()
        self.set_data()


    def set_data(self):
        self.year = self.localtime.tm_year
        self.month = self.localtime.tm_mon - 1
        self.day = self.localtime.tm_mday
        self.first_wday = datetime.datetime(self.year, self.month + 1, 1).weekday()
        self.current_year = self.year
        self.current_month = self.month
        self.current_data = True
        self.first_week = datetime.datetime(self.year, self.month + 1, 1).isocalendar().week % \
                          datetime.datetime(self.year - 1, 12, 31).isocalendar().week
        self.days_count = monthrange(self.year, self.month + 1)[1]

    def plus_month(self):
        self.year += (self.month + 1) // 12
        self.month = (self.month + 1) % 12
        if self.year == self.current_year and self.current_month == self.month:
            self.current_data = True
        else:
            self.current_data = False

    def minus_month(self):
        self.year += (self.month - 1) // 12
        self.month = (self.month - 1) % 12

        if self.year == self.current_year and self.current_month == self.month:
            self.current_data = True
        else:
            self.current_data = False