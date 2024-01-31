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
        """ experimenting with opacity 0.5
        alpha = image.split()[3]
        alpha = alpha.point(lambda i: i * 0.5)
        image.putalpha(alpha)
        """

        self.tk_image = ImageTk.PhotoImage(image)

        super().__init__(
            master, width=size, height=size, borderwidth=0, highlightthickness=0
        )

        self.color = color
        # the background is transparent by default, which is white in tkinter
        #self.configure(background="red")
        self.configure(background=master.background)

        # save col and row for easier manipulation on the board
        #self.col = (event.x - size // 2) // size + 1
        #self.row = (event.y - size // 2) // size + 1
        #self.place(x = self.col * size, y=self.row * size, anchor="center")
        new_x = ((event.x - master.offset + size // 2) // size) * size + master.offset
        new_y = ((event.y - master.offset + size // 2) // size) * size + master.offset
        self.place(x=new_x, y=new_y, anchor="center")
        self.create_image(0, 0, image=self.tk_image, anchor="nw")
