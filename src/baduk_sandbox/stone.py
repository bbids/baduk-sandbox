from tkinter import Canvas
from PIL import ImageTk
from PIL import Image


import logging
from .action_command import RemoveStone
from .event import EventWrapper


class Stone(Canvas):
    """Represents the stone on the board."""

    image_cache = {}

    def __init__(self, master, event_w, color):
        self.master = master
        self.color = color

        if color not in Stone.image_cache:
            Stone.image_cache[color] = self.load_stone_image(color)
        self.tk_image = Stone.image_cache[color]

        super().__init__(
            master,
            width=self.master.square_size,
            height=self.master.square_size,
            borderwidth=0,
            highlightthickness=0,
        )

        # we want to place on x and y based on mouse click
        if event_w.row is None and event_w.col is None:
            new_x, new_y = self.compute_x_and_y(event_w.event.x, event_w.event.y)
            self.row, self.col = self.compute_col_and_row(new_x, new_y)
            self.place(x=new_x, y=new_y, anchor="center")
        else:
            # we want to place based on some row and col
            self.row = event_w.row
            self.col = event_w.col

            board = self.master
            # offset is the distance from board edge to outermost gameboard line
            # rows and cols go from 1 onwards
            x = board.offset + board.square_size * (self.row - 1)
            y = board.offset + board.square_size * (self.col - 1)
            logging.debug(f"NEW WAY, X: {x}, Y: {y}")
            self.place(x=x, y=y, anchor="center")

        self.create_image(0, 0, image=self.tk_image, anchor="nw")

        # hide the default white background
        self.configure(background=master.gui.background)

        # remove stone 
        self.bind("<3>", lambda event: self.remove(event))

    def remove(self, event):
        event_w = EventWrapper(event)
        event_w.row = self.row
        event_w.col = self.col
        
        app = self.master.master
        RemoveStone(app, event_w).execute()

    def compute_x_and_y(self, x, y):
        """Based on received x and y relative to board canvas x and y,
        compute the suitable x"""
        board = self.master
        size = board.square_size
        offset = board.offset

        new_x = ((x - offset + size // 2) // size) * size + offset
        new_y = ((y - offset + size // 2) // size) * size + offset

        return new_x, new_y

    def compute_col_and_row(self, x, y):
        board = self.master
        return x // board.square_size, y // board.square_size

    def load_stone_image(self, color):
        match color:
            case "black":
                image_path = "assets/black.png"
            case "white":
                image_path = "assets/white.png"

        image = Image.open(image_path)
        size = self.master.square_size
        image = image.resize((size, size))
        return ImageTk.PhotoImage(image)

        """
        alpha = image.split()[3]
        alpha = alpha.point(lambda i: i * 0.5)
        image.putalpha(alpha)
        """

    def __repr__(self):
        return f"{self.color}"
