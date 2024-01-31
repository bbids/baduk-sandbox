from tkinter import Canvas
from PIL import ImageTk
from PIL import Image


class Stone(Canvas):
    """Represents the stone on the board."""

    def __init__(self, master, size, event, color):
        self.master = master

        match color:
            case "black":
                image = Image.open("black.png")
            case "white":
                image = Image.open("white.png")

        image = image.resize((27, 27))

        self.tk_image = ImageTk.PhotoImage(image)

        super().__init__(
            master, width=size - 1, height=size - 1, borderwidth=0, highlightthickness=0
        )

        self.color = color
        self.configure(background="#DBB072")

        # save col and row for easier manipulation on the board
        self.col = (event.x - size // 2) // size + 1
        self.row = (event.y - size // 2) // size + 1
        self.place(x=self.col * size, y=self.row * size, anchor="center")
        self.create_image(13, 13, image=self.tk_image, anchor="center", tags="stone")
