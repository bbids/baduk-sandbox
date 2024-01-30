from tkinter import *
from tkinter import ttk

class Mainframe(ttk.Frame):

    def __init__(self, master):
        self.master = master

        super().__init__(master, padding=10)

        self.grid(column=0, row=0, sticky=(N, W, E, S))



