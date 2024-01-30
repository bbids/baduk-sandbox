from tkinter import Canvas

class Board(Canvas):
    """Represents the whole game board for the baduk game."""

    def __init__(self, master):
        self.master = master

        # stones also get places on the edge, so we need offset
        self.offset = 28
        self.square_edge = 28
        # 28 * 18 = 504 this is for squares or 19 lines
        self.line_size = 504 

        # canvas width and height, accessible via tkinter
        width = self.line_size + 2 * self.offset
        height = self.line_size + 2 * self.offset

        # have to reset borderwidth and thickness so that lines are shown on top and left
        super().__init__(master, width=width, height=height, borderwidth=0, highlightthickness=0)
        self.grid(column=0, row=0, padx=50, pady=50)
        self.configure(background="#DBB072")

        # horizontal lines
        for i in range(0, self.line_size + 1, self.square_edge):
            i += self.offset
            self.create_line(self.offset, i, self.line_size + self.offset, i, fill="black", width=2)

        # vertical lines
        for i in range(0, self.line_size + 1, self.square_edge):
            i += self.offset
            self.create_line(i, self.offset, i, self.line_size + self.offset, fill="black", width=2)

        # add event listener
        self.bind("<1>", self.on_board_click)

    def on_board_click(self, event):
        """Event listener for the board - wooden part only"""
        se = self.square_edge
        off = self.offset

        # ignore offset
        x_cond = (off - se / 2) < event.x < (self.line_size + off + se/ 2)
        y_cond = (off - se / 2) < event.y < (self.line_size + off + se / 2)
        if (x_cond and y_cond):

            # stone class
            # save x and y to game state for save

            stone = Canvas(self, width=se - 1, height=se - 1)
            stone.configure(background="black")
            new_x = (event.x - se // 2) // se * se + se
            new_y = (event.y - se // 2) // se * se + se
            stone.place(x=new_x, y=new_y, anchor="center")
            print(f"Board clicked at x={event.x}, y={event.y}")



