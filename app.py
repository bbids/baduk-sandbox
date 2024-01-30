from tkinter import *
from tkinter import ttk

class App(Tk):

    def __init__(self):
        super().__init__()

        self.title("Baduk-sandbox")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight = 1)