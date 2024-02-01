import tkinter as tk
import logging

from .mainframe import Mainframe
from .board import Board
from .side_menu import SideMenu
from .command import PlaceStone
from .command_history import CommandHistory

class App(tk.Tk):
    """Manage the UI components, act as an invoker and the client."""
    def __init__(self):
        super().__init__()

        self.title("Baduk-sandbox")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.mainframe = Mainframe(self)
        self.side_menu = SideMenu(self.mainframe)
        self.board = Board(self.mainframe)

        self.history = CommandHistory()

        self.board.bind("<1>", lambda event: self.execute_command(PlaceStone(self.board), event))

    def execute_command(self, command, event):
        if (command.execute(event)):
            self.history.push(command)

        logging.info(f"Command history: {self.history}")

    def undo_command(self):
        assert self.history.size() > 0
        self.history.pop().undo()


def start_app() -> App:
    logging.basicConfig(level=logging.DEBUG)
    root = App()
    return root
        
