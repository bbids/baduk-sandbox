from tkinter import Canvas
from PIL import ImageTk
from PIL import Image


import logging


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

        # place and show image
        new_x, new_y, self.row, self.col = self.get_placement(event_w.event.x, event_w.event.y)
        self.place(x=new_x, y=new_y, anchor="center")
        self.create_image(0, 0, image=self.tk_image, anchor="nw")

        # hide the default white background
        self.configure(background=master.gui.background)

    @staticmethod
    def compute_place(board, x, y):
        """Based on received x and y relative to board canvas x and y,
        compute the suitable x"""
        size = board.square_size
        offset = board.offset

        new_x = ((x - offset + size // 2) // size) * size + offset
        new_y = ((y - offset + size // 2) // size) * size + offset

        return new_x, new_y

    @staticmethod
    def compute_col_and_row(board, x, y):
        return x // board.square_size, y // board.square_size

    def get_placement(self, x, y):
        """Handle stone placement based on event x and y relative to board canvas

        Returns: x, y, row, col
        """
        new_x, new_y = Stone.compute_place(self.master, x, y)

        row, col = Stone.compute_col_and_row(self.master, new_x, new_y)

        logging.debug(f"Row: {row} Col: {col}")
        return (new_x, new_y, row, col)

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
