from tkinter import *
from tkinter import ttk

from utility import save
from utility import reset


class SideMenu(ttk.Frame):
    """Represents the app's side menu. Includes all the buttons"""

    def __init__(self, master):
        self.master = master

        super().__init__(master, width=200, height=400, padding=(20, 100))
        self.grid(column=1, row=0, sticky=(W, E))
        
        save_btn = ttk.Button(self, text="Save", command=save)
        save_btn.grid(column=0, row=0, sticky=W, padx=(10, 10))

        reset_btn = ttk.Button(self, text="Reset", command=reset)
        reset_btn.grid(column=1, row=0, sticky=E, padx=(10, 10))
