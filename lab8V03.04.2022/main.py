#Author for SecondsToDays:Amanda Stein 
#Author for Time Calculator: Olga Sotiriadi
#Editor for Main: Amanda Stein Author: Professor
#Class 133y
#lab 8
#Purpose: To edit the main file run the new changes to the starter code.
# Version 03.04.2022

import tkinter as tk
import tkinter.ttk as ttk

from AboutApp import AboutApp
from time_calculator import TimecalcApp
from SecondsToDays import SecondsToDaysApp

# Main Window for the team calculator project.
# To add a new tab, create an App object with a get_top_frame method.
# Then, add the app to the __main_notebook, along with a name for the tab.
# See GramsToOuncesApp.py for a simple example.

class MainApp:
    def __init__(self, master):
        # This is needed to allow the notebook tabs to stretch.
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        # build ui
        self.__main_notebook = ttk.Notebook(master)
        self.__main_notebook.grid(column='0', row='0', sticky='nsew')
        self.__main_notebook.rowconfigure('0', weight='1')
        self.__main_notebook.columnconfigure('0', weight='1')

        # Main widget
        self.__mainwindow = self.__main_notebook

        # Add About... tab
        about_app = AboutApp(self.__mainwindow)
        self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        # Add first calculator
        time_calculator_app = TimecalcApp(self.__mainwindow)
        self.__main_notebook.add(time_calculator_app.get_top_frame(), text = 'Days to Seconds')
        

        # Add Second 
        seconds_to_days_app = SecondsToDaysApp(self.__mainwindow)
        self.__main_notebook.add(seconds_to_days_app.get_top_frame(), text ='Seconds to days')


    def run(self):
        self.__mainwindow.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    app.run()

