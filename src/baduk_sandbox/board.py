from tkinter import Canvas
import logging

from .stone import Stone


class Board(Canvas):
    """Represents the game board of size 19x19 for the baduk game."""

    def __init__(self, master, board_size=19, background="#DBB072"):
        self.master = master
        self.board_size = board_size
        self.background = background
        self.map = [[None for _ in range(board_size)] for _ in range(board_size)]

        # 504 is divisible by 18, 12 and 8 - this allows for board sizes of 19, 13 and 9
        self.line_size = 504
        # there are board_size - 1 squares, and board_size lines
        self.square_size = self.line_size // (board_size - 1)
        # offset for aesthetics, because stones can get placed on the edge
        self.offset = self.square_size # + 11

        # canvas width and height, later accessible via tkinter
        width = self.line_size + 2 * self.offset
        height = self.line_size + 2 * self.offset

        # have to reset borderwidth and thickness so that lines are shown on top and left
        super().__init__(
            master, width=width, height=height, borderwidth=0, highlightthickness=0
        )
        self.grid(column=0, row=0, padx=50, pady=50)
        self.configure(background=self.background)

        self.draw_horizontal_lines()
        self.draw_vertical_lines()
        self.draw_star_points()

        # event listener for stones
        self.bind("<1>", lambda event: self.on_board_click(event, "black"))
        self.bind("<3>", lambda event: self.on_board_click(event, "white"))

    def draw_star_points(self):
        match self.board_size:
            case 19:
                rows = [3, 9, 15]
                cols = [3, 9, 15]
            case 9:
                rows = [4]
                cols = [4]
            case _:
                logging.error("Board size not supported!")
        for row in rows:
            for col in cols:
                x = row * self.square_size + self.offset
                y = col * self.square_size + self.offset
                radius = self.square_size // 7

                self.create_oval(
                    x - radius, y - radius, x + radius, y + radius, fill="black"
                )

    def draw_horizontal_lines(self):
        for i in range(0, self.line_size + 1, self.square_size):
            i += self.offset
            self.create_line(
                self.offset, i, self.line_size + self.offset, i, fill="black", width=2
            )

    def draw_vertical_lines(self):
        for i in range(0, self.line_size + 1, self.square_size):
            i += self.offset
            self.create_line(
                i, self.offset, i, self.line_size + self.offset, fill="black", width=2
            )

    def on_board_click(self, event, color):
        """Event listener for the board - wooden part only"""
        se = self.square_size
        off = self.offset

        logging.debug(f"x: {event.x}")
        logging.debug(f"y: {event.y}")


        # ignore offset
        x_cond = (off - se / 2) < event.x < (self.line_size + off + se / 2)
        y_cond = (off - se / 2) < event.y < (self.line_size + off + se / 2)
        if x_cond and y_cond:
            stone = Stone(self, se, event, color)
            self.map[stone.row - 1][stone.col - 1] = stone
            # test the map
            logging.debug(f"Row in board: {stone.row - 1}")
            logging.debug(f"Col in board: {stone.col - 1}")
            logging.debug(self.map[stone.row - 1][stone.col - 1])

        logging.debug(f"Board clicked at x={event.x}, y={event.y}")
