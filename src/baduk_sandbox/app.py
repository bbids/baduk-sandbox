import tkinter as tk
import logging

from .mainframe import Mainframe
from .board import Board
from .side_menu import SideMenu
from .action_command import PlaceStone
from .command_history import CommandHistory
from .stone_placement import StonePlacement


class App(tk.Tk):
    """Manage the UI components, act as an action command invoker and client."""

    def __init__(self):
        super().__init__()

        self.title("Baduk-sandbox")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # UI components
        self.mainframe = Mainframe(self)
        self.board = Board(self.mainframe)
        self.side_menu = SideMenu(self.mainframe)

        self.stone_colorer = StonePlacement(alternate=True, initial_color="black")
        self.history = CommandHistory()

        self.board.bind(
            "<1>", lambda event: self.execute_command(PlaceStone(self), event)
        )

    def execute_command(self, command, event = None):
            command.execute(event)
            self.history.push(command)
            self.stone_colorer.toggle_color()

    def undo_command(self):
        assert self.history.size() > 0
        self.history.pop().undo()
        self.stone_colorer.toggle_color()


def start_app() -> App:
    logging.basicConfig(level=logging.DEBUG)
    root = App()
    return root
