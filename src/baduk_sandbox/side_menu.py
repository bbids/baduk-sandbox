import tkinter as tk
from tkinter import ttk

from .utility import save
from .utility import reset
from .utility import load

from .ui_command import BlackCommand
from .ui_command import WhiteCommand


class SideMenu(ttk.Frame):
    """Represents the app's side menu, acts as an UI commands invoker and client"""

    def __init__(self, master):
        self.master = master
        self.app = master.master

        super().__init__(master, width=200, height=400, padding=(20, 100))
        self.grid(column=1, row=0, sticky=(tk.W, tk.E))

        self.create_button("Save", save, column=0, row=0, sticky=tk.W)
        self.create_button("Load", load, column=1, row=0, sticky=tk.E)
        self.create_button(
            "Black",
            BlackCommand(self.app).execute,
            column=0,
            row=1,
            sticky=tk.W,
        )
        self.create_button(
            "White",
            WhiteCommand(self.app).execute,
            column=1,
            row=1,
            sticky=tk.E,
        )
        self.create_button("Undo", self.app.undo_command, column=0, row=2, sticky=tk.W)
        self.create_button("Reset", reset, column=1, row=2, sticky=tk.E)

    def create_button(self, text, command, column, row, sticky):
        button = ttk.Button(self, text=text, command=command)
        button.grid(column=column, row=row, sticky=sticky, padx=(10, 10), pady=50)
