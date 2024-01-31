import tkinter as tk
from tkinter import ttk

from src.utility import save
from src.utility import reset
from src.utility import load
from src.utility import undo
from src.utility import black
from src.utility import white


class SideMenu(ttk.Frame):
    """Represents the app's side menu. Includes all the buttons"""

    def __init__(self, master):
        self.master = master

        super().__init__(master, width=200, height=400, padding=(20, 100))
        self.grid(column=1, row=0, sticky=(tk.W, tk.E))

        save_btn = ttk.Button(self, text="Save", command=save)
        save_btn.grid(column=0, row=0, sticky=tk.W, padx=(10, 10), pady=50)

        load_btn = ttk.Button(self, text="Load", command=load)
        load_btn.grid(column=1, row=0, sticky=tk.E, padx=(10, 10), pady=50)

        black_btn = ttk.Button(self, text="Black", command=black)
        black_btn.grid(column=0, row=1, sticky=tk.W, padx=(10, 10), pady=50)

        white_btn = ttk.Button(self, text="White", command=white)
        white_btn.grid(column=1, row=1, sticky=tk.E, padx=(10, 10), pady=50)

        undo_btn = ttk.Button(self, text="Undo", command=undo)
        undo_btn.grid(column=0, row=2, sticky=tk.W, padx=(10, 10), pady=50)

        reset_btn = ttk.Button(self, text="Reset", command=reset)
        reset_btn.grid(column=1, row=2, sticky=tk.E, padx=(10, 10), pady=50)
