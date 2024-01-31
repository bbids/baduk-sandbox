from tkinter import Canvas
import logging

class Stone(Canvas):
    """Represents the stone on the board. """

    def __init__(self, master, size, event, color):
        self.master = master
        super().__init__(master, width=size- 1, height=size- 1)
        self.configure(background=color)
        
        # save col and row for easier manipulation on the board
        self.col= (event.x - size // 2) // size + 1
        self.row = (event.y - size // 2) // size + 1
        self.place(x=self.col * size, y=self.row * size, anchor="center")

