class Translate:
    """Translate board mouse clicks event coordinates to row and col"""

    def __init__(self, board, x, y):
        self._board = board
        self._x = x
        self._y = y

    def get_col_and_row(self):
        if self.is_valid_spot():
            self.adjust_x_and_y()
            return self.compute_col_and_row()
        return None

    def is_valid_spot(self):
        """Check if a stone can be placed here."""
        board = self._board
        se = board.square_size
        off = board.offset

        x_cond = (off - se / 2) < self._x < (board.line_size + off + se / 2)
        y_cond = (off - se / 2) < self._y < (board.line_size + off + se / 2)

        return x_cond and y_cond

    def adjust_x_and_y(self):
        """Moves x and y to nearest cross section"""
        board = self._board
        size = board.square_size
        offset = board.offset

        self._x = ((self._x - offset + size // 2) // size) * size + offset
        self._y = ((self._y - offset + size // 2) // size) * size + offset

    def compute_col_and_row(self):
        """Compute col and row from coordinates on crossection"""
        board = self._board
        self._col = self._x // board.square_size
        self._row = self._y // board.square_size
        return self._col, self._row

    @property
    def col(self):
        return self._col

    @property
    def row(self):
        return self._row
