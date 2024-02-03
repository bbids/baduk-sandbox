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
        self._placement_sound = tkSnack.Sound()
        self.placement_sound.read("assets/stone_placement.wav")

        # UI components
        self._board = Board(self)
        self._side_menu = SideMenu(self)

        self._play_mode = PlayMode()
        self.play_mode.game_start()
        self._history = CommandHistory()

    def undo_command(self):
        if self.history.size() <= 0:
            logging.error("NO HISTORY")
            return None
        
        cmnd = self.history.pop()
        cmnd.undo()

        if isinstance(cmnd, PlaceStone):
            self.play_mode.toggle_color

    @property
    def history(self):
        return self._history
    
    @property
    def play_mode(self):
        return self._play_mode
    
    @property
    def board(self):
        return self._board
    
    @property
    def side_menu(self):
        return self._side_menu
    
    @property
    def placement_sound(self):
        return self._placement_sound
        


def start_app() -> App:
    logging.basicConfig(level=logging.DEBUG)
    root = App()
    return root
