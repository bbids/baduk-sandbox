from tkinter import Canvas
from PIL import ImageTk
from PIL import Image


class Stone(Canvas):
    """Represents the stone on the board."""

    def __init__(self, master, size, event, color):
        self.master = master

        match color:
            case "black":
                image = Image.open("assets/black.png")
            case "white":
                image = Image.open("assets/white.png")

        image = image.resize((size, size))

        self.tk_image = ImageTk.PhotoImage(image)

        super().__init__(
            master, width=size, height=size, borderwidth=0, highlightthickness=0
        )

        self.color = color
        # the background is transparent by default, which is white in tkinter
        self.configure(background=master.background)

        # save col and row for easier manipulation on the board
        self.col = (event.x - size // 2) // size + 1
        self.row = (event.y - size // 2) // size + 1
        self.place(x=self.col * size, y=self.row * size, anchor="center")
        self.create_image(0, 0, image=self.tk_image, anchor="nw")
