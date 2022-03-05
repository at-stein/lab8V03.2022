# Author: Olga Sotiriadi
# Lab:8
# Date:03.04.2022
# Purpose: Time Calculator
import pathlib
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import tkinter.messagebox as mb

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "TimeCalc.ui"


class TimecalcApp:
    SEC_PER_DAY = 86400
    SEC_PER_HOUR = 3600
    SEC_PER_MIN = 60

    def __init__(self, master=None):
        # Boilerplate to build the tkinter interface based on TimeCalc.ui
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object('top_level', master)
        builder.connect_callbacks(self)

        # Save these UI elements as properties so that we can access them when
        # the user clicks on the calculate button.
        self.__days_entry = builder.get_object('days_entry', master)
        self.__hours_entry = builder.get_object('hours_entry', master)
        self.__minutes_entry = builder.get_object('minutes_entry', master)
        self.__seconds_entry = builder.get_object('seconds_entry', master)
        self.__result_entry_variable = builder.get_variable('result_entry_variable')


    def calculate(self):
        # Convert days, hours, minutes and seconds to seconds. If there's an error, display an error message.
        try:
            days = float(self.__days_entry.get())
            hours = float(self.__hours_entry.get())
            minutes = float(self.__minutes_entry.get())
            seconds = float(self.__seconds_entry.get())
            total_seconds = self.SEC_PER_DAY * days + self.SEC_PER_HOUR * hours + self.SEC_PER_MIN * minutes + seconds
            self.__result_entry_variable.set("{:.2f} seconds".format(total_seconds))
        except ValueError:
            mb.showerror(title="Error Calculating!", message="Please try again.")

    def run(self):
        self.__mainwindow.mainloop()

    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a tabbed notebook.
        return self.__mainwindow

    def clear(self):
        self.__days_entry.delete(0, tk.END)
        self.__hours_entry.delete(0, tk.END)
        self.__minutes_entry.delete(0, tk.END)
        self.__seconds_entry.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Time Calculator")
    app = TimecalcApp(root)
    app.run()








