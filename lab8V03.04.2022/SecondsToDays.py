#Author: Amanda Stein
#Class 133y
#lab 8
# Version 03.2.2022
#Purpose: To take the seconds of a day and convert it to day, hour, minute and second.

import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import tkinter.messagebox as mb

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "seconds_to_days.ui"


class SecondsToDaysApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('base_frame', master)
        builder.connect_callbacks(self)
        self.__entry_user = builder.get_object('entry_user', master)
        self.__result_entry_variable = builder.get_variable('result_entry_variable')

    def run(self):
        self.__mainwindow.mainloop()

    def calculate(self):
        minutesInHour = 60
        hoursInDay = 24
        secondsInAnHour = 3600
        time = float(self.__entry_user.get())
        # the conversion
        if time > 0:
            days = time // (hoursInDay * secondsInAnHour)
            time = time % (hoursInDay * secondsInAnHour)
            hours = time // secondsInAnHour
            time %= secondsInAnHour
            minutes = time // minutesInHour
            time %= minutesInHour
            seconds = time
            self.__result_entry_variable.set("Days:%d Hours:%d Minutes:%d Seconds:%d " % (days, hours, minutes, seconds))
        else:
            time < 0
            print("Please enter a number greater than 0")

    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a tabbed notebook.
        return self.__mainwindow

if __name__ == '__main__':
    root = tk.Tk()
    app = SecondsToDaysApp(root)
    app.run()
