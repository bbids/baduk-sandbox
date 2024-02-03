from tkinter import Canvas
import logging

from .stone import Stone
from .board_GUI import BoardGUI
from .action_command import PlaceStone
from .board_click import Translate


class Board(Canvas):
    """Represents the game board"""

    def __init__(self, master, board_size=19, background="#DBB072"):
        self.master = master
        self._board_size = board_size
        self._board_map = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

        self.configure_board()

        canvas_size = self.line_size + 2 * self.offset
        super().__init__(
            master,
            width=canvas_size,
            height=canvas_size,
            # have to reset borderwidth and thickness so that lines are shown on top and left
            borderwidth=0,
            highlightthickness=0,
        )

        # handle the gui in a seperate space
        self._gui = BoardGUI(self, background)

        # handle stone placement
        self.bind("<1>", lambda event: PlaceStone(self.master, event).execute())

    def configure_board(self):
        # 504 is divisible by 18, 12 and 8 - this allows for board sizes of 19, 13 and 9
        # because there are board_size - 1 squares, and board_size lines
        # offset is there because we want to detect clicks from a bit outside last line
        self._line_size = 504
        self._square_size = self.line_size // (self.board_size - 1)
        self._offset = self.square_size    

    def place_stone(self, event_w):
        if event_w.row is None:
            translator = Translate(self, event_w.event.x, event_w.event.y)
            success = translator.get_col_and_row()
            if success:
                event_w.col, event_w.row = success

        stone_color = self.master.play_mode.color

        stone = Stone(self, event_w.col, event_w.row, stone_color)
        self.board_map[event_w.row - 1][event_w.col - 1] = stone

        self.master.placement_sound.play()
        self.master.play_mode.toggle_color()

        return True

    def remove_stone(self, event_w):
        if not (hasattr(event_w, "row") and hasattr(event_w, "col")):
            logging.error("???")
        self.board_map[event_w.row - 1][event_w.col - 1].destroy()
        self.board_map[event_w.row - 1][event_w.col - 1] = None
        self.master.play_mode.toggle_color()
        return True

    def clear(self):
        """Clear the board - remove all the stones"""
        for r in range(len(self.board_map)):
            for c in range(len(self.board_map[r])):
                if self.board_map[r][c] is not None:
                    self.board_map[r][c].destroy()
                    self.board_map[r][c] = None

    @property
    def board_size(self):
        return self._board_size

    @property
    def board_map(self):
        return self._board_map

    @property
    def square_size(self):
        return self._square_size
    
    @property
    def line_size(self):
        return self._line_size

    @property
    def offset(self):
        return self._offset
    
    @property
    def gui(self):
        return self._gui

