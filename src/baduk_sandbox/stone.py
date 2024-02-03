from tkinter import Canvas
from PIL import ImageTk
from PIL import Image


import logging
from .action_command import RemoveStone
from .event import EventWrapper


class Stone(Canvas):
    """Represents the stone on the board."""

    image_cache = {}

    def __init__(self, master, col, row, color):
        self.master = master
        self.color = color
        self.col = col
        self.row = row


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

        self.show()

        self.bind("<3>", lambda event: self.remove(event))

    def show(self):
        """Handle stone placement"""

        board = self.master
        x = board.offset + board.square_size * (self.col - 1)
        y = board.offset + board.square_size * (self.row - 1)
        self.place(x=x, y=y, anchor="center")

        # nw to adjust our image of the stone
        self.create_image(0, 0, image=self.tk_image, anchor="nw")

        # hide the default white background, use board background
        self.configure(background=self.master.gui.background)


    def remove(self, event):
        event_w = EventWrapper(event)
        event_w.row = self.row
        event_w.col = self.col
        
        app = self.master.master
        RemoveStone(app, event_w).execute()

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
