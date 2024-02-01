import logging


class BoardGUI():
    """Represents the baduk game board gui."""

    def __init__(self, board, background="#DBB072"):
        self.background = background

        board.grid(column=0, row=0, padx=50, pady=50)
        board.configure(background=self.background)

        BoardGUI.draw_horizontal_lines(board)
        BoardGUI.draw_vertical_lines(board)
        BoardGUI.draw_star_points(board)

    @staticmethod
    def draw_star_points(board):
        match board.board_size:
            case 19:
                rows = [3, 9, 15]
                cols = [3, 9, 15]
            case 9:
                rows = [4]
                cols = [4]
            case _:
                logging.error("Board size not supported!")
        for row in rows:
            for col in cols:
                x = row * board.square_size + board.offset
                y = col * board.square_size + board.offset
                radius = board.square_size // 7

                board.create_oval(
                    x - radius, y - radius, x + radius, y + radius, fill="black"
                )

    @staticmethod
    def draw_horizontal_lines(board):
        for i in range(0, board.line_size + 1, board.square_size):
            i += board.offset
            board.create_line(
                board.offset, i, board.line_size + board.offset, i, fill="black", width=2
            )

    @staticmethod
    def draw_vertical_lines(board):
        for i in range(0, board.line_size + 1, board.square_size):
            i += board.offset
            board.create_line(
                i, board.offset, i, board.line_size + board.offset, fill="black", width=2
            )

