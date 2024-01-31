from tkinter import Canvas
import logging

from stone import Stone


class Board(Canvas):
    """Represents the game board of size 19x19 for the baduk game."""

    def __init__(self, master):
        self.master = master

        board_size = 19
        self.map = [[None for _ in range(board_size)] for _ in range(board_size)]

        # 504 is divisible by 18, 12 and 8
        # this allows for board sizes of 19, 13 and 9
        self.line_size = 504 
        # there are board_size - 1 squares, and board_size lines
        self.square_size = self.line_size // (board_size - 1)
        # offset for aesthetics, because stones can get placed on the edge
        self.offset = self.square_size

        # canvas width and height, later accessible via tkinter
        width = self.line_size + 2 * self.offset
        height = self.line_size + 2 * self.offset

        # have to reset borderwidth and thickness so that lines are shown on top and left
        super().__init__(master, width=width, height=height, borderwidth=0, highlightthickness=0)
        self.grid(column=0, row=0, padx=50, pady=50)
        self.configure(background="#DBB072")

        self.draw_horizontal_lines()
        self.draw_vertical_lines()

        # event listener for stones
        self.bind("<1>", lambda event: self.on_board_click(event, "black"))
        self.bind("<3>", lambda event: self.on_board_click(event, "white"))

    def draw_horizontal_lines(self):
        for i in range(0, self.line_size + 1, self.square_size):
            i += self.offset
            self.create_line(self.offset, i, self.line_size + self.offset, i, fill="black", width=2)

    def draw_vertical_lines(self):
        for i in range(0, self.line_size + 1, self.square_size):
            i += self.offset
            self.create_line(i, self.offset, i, self.line_size + self.offset,       fill="black", width=2)

    def on_board_click(self, event, color):
        """Event listener for the board - wooden part only"""
        se = self.square_size
        off = self.offset

        # ignore offset
        x_cond = (off - se / 2) < event.x < (self.line_size + off + se / 2)
        y_cond = (off - se / 2) < event.y < (self.line_size + off + se / 2)
        if (x_cond and y_cond):
            stone = Stone(self, se, event, color)
            self.map[stone.row - 1][stone.col - 1] = stone

        logging.debug(f"Board clicked at x={event.x}, y={event.y}")


