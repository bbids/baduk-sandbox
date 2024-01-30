from tkinter import Canvas
from tkinter import ttk

class Board(Canvas):

    def __init__(self, master):
        self.master = master
        offset = 28
        self.offset = offset
        line_size = 504
        self.line_size = line_size
        width = line_size + 2 * offset
        height = line_size + 2 * offset
        square_edge = 28 # 28 * 18 = 504
        self.square_edge = square_edge

        # have to reset borderwidth and thickness so that lines are shown on top and left
        super().__init__(master, width=width, height=height, borderwidth=0, highlightthickness=0)
        self.grid(column=0, row=0, padx=50, pady=50)
        self.configure(background="#DBB072")

        # horizontal lines
        for i in range(0, line_size + 1, square_edge):
            i += offset
            self.create_line(offset, i, line_size + offset, i, fill="black", width=2)

        # vertical lines
        for i in range(0, line_size + 1, square_edge):
            i += offset
            self.create_line(i, offset, i, line_size + offset, fill="black", width=2)

        # add event listener
        self.bind("<1>", self.on_board_click)

    def on_board_click(self, event):
        se = self.square_edge
        off = self.offset
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



