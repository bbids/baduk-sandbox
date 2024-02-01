from tkinter import Canvas
import logging

from .stone import Stone
from .board_GUI import BoardGUI


class Board(Canvas):
    """Represents the game board"""

    def __init__(self, master, board_size=19, background="#DBB072"):
        self.master = master
        self.board_size = board_size

        self.map = [[None for _ in range(board_size)] for _ in range(board_size)]

        # 504 is divisible by 18, 12 and 8 - this allows for board sizes of 19, 13 and 9
        # because there are board_size - 1 squares, and board_size lines
        # offset is for aesthetics, because stones can get placed on the outermost lines
        self.line_size = 504
        self.square_size = self.line_size // (board_size - 1)
        self.offset = self.square_size

        canvas_size = self.line_size + 2 * self.offset
        # have to reset borderwidth and thickness so that lines are shown on top and left
        super().__init__(
            master,
            width=canvas_size,
            height=canvas_size,
            borderwidth=0,
            highlightthickness=0,
        )

        # handle the gui in a seperate space
        self.gui = BoardGUI(self, background)

    def place_stone(self, event, stone_color="black"):
        """Handle the stone placement event. 
        
        Returns stone column and row if valid, else None.
        """
        logging.debug(f"Board clicked at x={event.x}, y={event.y}")

        se = self.square_size
        off = self.offset

        # ignore offset
        x_cond = (off - se / 2) < event.x < (self.line_size + off + se / 2)
        y_cond = (off - se / 2) < event.y < (self.line_size + off + se / 2)
        if x_cond and y_cond:
            stone = Stone(self, event, stone_color)
            self.map[stone.row - 1][stone.col - 1] = stone
            # test the map
            # logging.debug(f"Row in board: {stone.row - 1}")
            # logging.debug(f"Col in board: {stone.col - 1}")
            # logging.debug(self.map[stone.row - 1][stone.col - 1])
            return stone.row, stone.col
        return None
