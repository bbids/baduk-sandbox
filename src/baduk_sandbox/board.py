from tkinter import Canvas
import logging

from .stone import Stone
from .board_GUI import BoardGUI
from .action_command import PlaceStone


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

        # handle stone placement
        self.bind(
            "<1>", lambda event: PlaceStone(self.master, event).execute()
        )

    def is_valid_spot(self, x, y):
        """Get x and y relative to board canvas, and check if a stone can be placed here."""
        se = self.square_size
        off = self.offset

        x_cond = (off - se / 2) < x < (self.line_size + off + se / 2)
        y_cond = (off - se / 2) < y < (self.line_size + off + se / 2)

        return x_cond and y_cond

    def place_stone(self, event_w):
        """Handle the stone placement event. 
        
        Returns bool value depending if stone was successfuly placed
        """
        x = event_w.event.x
        y = event_w.event.y
        logging.debug(f"Board clicked at x={x}, y={y}")


        stone_color = self.master.play_mode.color

        if self.is_valid_spot(x, y):
            stone = Stone(self, event_w, stone_color)

            self.map[stone.row - 1][stone.col - 1] = stone
            self.master.placement_sound.play()
            self.master.play_mode.toggle_color()

            event_w.row = stone.row
            event_w.col = stone.col

            return True
        
        return False
    
    def remove_stone(self, event_w):
        self.map[event_w.row - 1][event_w.col - 1].destroy()
        self.map[event_w.row - 1][event_w.col - 1] = None
        return True


    def clear(self):
        """Clear the board"""
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if self.map[r][c] is not None:
                    self.map[r][c].destroy()
                    self.map[r][c] = None
    