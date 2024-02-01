from tkinter import Canvas
from PIL import ImageTk
from PIL import Image

import logging


class Stone(Canvas):
    """Represents the stone on the board."""
    image_cache = {}

    def __init__(self, master, event, color):
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
            highlightthickness=0
        )

        # place and show image
        new_x, new_y, self.col, self.row = self.compute_placement(event.x, event.y)
        self.place(x=new_x, y=new_y, anchor="center")
        self.create_image(0, 0, image=self.tk_image, anchor="nw")

        # hide the default white background
        self.configure(background=master.gui.background)

    def compute_placement(self, x, y):
        """Find the spot on the board on which to place the stone.
        
        Returns: x, y, row, col
        """
        master = self.master
        size = master.square_size

        new_x = ((x - master.offset + size // 2) // size) * size + master.offset
        new_y = ((y - master.offset + size // 2) // size) * size + master.offset

        # we also save row and col for a map of all the stones and convenience
        row = new_y // size
        col = new_x // size

        logging.debug(f"Row: {row}")
        logging.debug(f"Col: {col}")

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
