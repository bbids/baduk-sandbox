import tkinter as tk
from tkinter import ttk

from .utility import save
from .utility import load

from .ui_command import BlackCommand
from .ui_command import WhiteCommand
from .ui_command import AlternateCommand
from .ui_command import ResetCommand


class SideMenu(ttk.Frame):
    """Represents the app's side menu, acts as an UI commands invoker and client"""

    def __init__(self, master):
        self.master = master

        super().__init__(master, width=200, height=400, padding=(20, 100))
        self.grid(column=1, row=0, sticky=(tk.W, tk.E))

        # active button should be highlighted
        active_style = ttk.Style()
        active_style.configure("Active.TButton", borderwidth="2", font=("calibri", 10, "bold"))
        self.active_button = None

        # stylize the default ttk Button
        default_style = ttk.Style()
        default_style.configure("TButton", focuscolor="none")

        self.create_button("Save", save, column=0, row=0, sticky=tk.W)
        self.create_button("Load", load, column=1, row=0, sticky=tk.E)

        self.create_button(
            "Black",
            BlackCommand(self.master).execute,
            column=0,
            row=1,
            sticky=tk.W,
        )
        self.create_button(
            "White",
            WhiteCommand(self.master).execute,
            column=1,
            row=1,
            sticky=None,
        )
        self.alternate_btn = self.create_button(
            "Alternate",
            AlternateCommand(self.master).execute,
            column=2,
            row=1,
            sticky=tk.E
        )
        self.alternate_btn["style"] = "Active.TButton"
        self.active_button = self.alternate_btn

        self.create_button("Undo", self.master.undo_command, column=0, row=2, sticky=tk.W)
        self.create_button(
            "Reset", ResetCommand(self.master).execute, column=1, row=2, sticky=tk.E
        )

    def create_button(self, text, command, column, row, sticky):
        def button_click_handler():
            if row == 1:
                self.active_button["style"] = "TButton"
                button["style"] = "Active.TButton"
                self.active_button = button
                
            command()

        button = ttk.Button(self, text=text, command=button_click_handler)
        button.grid(column=column, row=row, sticky=sticky, padx=(10, 10), pady=50)

        return button
