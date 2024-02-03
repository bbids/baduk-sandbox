import tkinter as tk
import logging
import tkSnack

from .board import Board
from .side_menu import SideMenu
from .action_command import PlaceStone
from .command_history import CommandHistory
from .play_mode import PlayMode


class App(tk.Tk):
    """Manage the UI components"""

    def __init__(self):
        super().__init__()
        self.title("Baduk-sandbox")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Sound management
        tkSnack.initializeSnack(self)
        self.placement_sound = tkSnack.Sound()
        self.placement_sound.read("assets/stone_placement.wav")

        # UI components
        self.board = Board(self)
        self.side_menu = SideMenu(self)

        self.play_mode = PlayMode()
        self.play_mode.game_start()
        self.history = CommandHistory()

    def undo_command(self):
        assert self.history.size() > 0
        cmnd = self.history.pop()
        cmnd.undo()

        if isinstance(cmnd, PlaceStone):
            self.play_mode.toggle_color
        


def start_app() -> App:
    logging.basicConfig(level=logging.DEBUG)
    root = App()
    return root
