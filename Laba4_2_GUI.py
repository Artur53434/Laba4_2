from ast import Lambda
from cProfile import label 
from tkinter import ttk
from turtle import width
from venv import create
from MainForm import MainForm
from styles import configure_styles
import button_logic
import locale

from CyclicQueue import CyclicQueue

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    main_form = MainForm()