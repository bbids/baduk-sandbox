import tkinter as tk

from .mainframe import Mainframe
from .board import Board
from .side_menu import SideMenu

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Baduk-sandbox")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


        self.mainframe = Mainframe(self)

        self.side_menu = SideMenu(self.mainframe)
        self.board = Board(self.mainframe)
