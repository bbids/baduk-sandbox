import unittest
import tkinter as tk

from src.baduk_sandbox.app import start_app
from src.baduk_sandbox.action_command import PlaceStone

class TestLogic(unittest.TestCase):
    """Test"""
    pass

'''
class TestBoardSandbox(unittest.TestCase):
    """Mainly placement of stone in sandbox mode, no game logic"""

    def setUp(self):
        self.app = start_app()

    def tear_down(self):
        self.app.destroy()

    def test_col_row(self):
        def_x = self.app.board.offset - self.app.board.square_size // 2 + 1
        def_y = self.app.board.offset - self.app.board.square_size // 2 + 1

        event = tk.Event()
        for row in range(19):
            for col in range(19):
                # None at beginning
                self.assertIsNone(self.app.board.map[col][row], None)

                # Casual placement
                event.x = def_x + self.app.board.square_size * col
                event.y = def_y + self.app.board.square_size * row
                self.app.execute_command(PlaceStone(self.app), event)
                self.assertIsNot(self.app.board.map[col][row], None)

    def test_col_row_invalid(self):
        event = tk.Event()
        event.x = -1
        event.y = -1
        for row in range(19):
            for col in range(19):
                self.app.execute_command(PlaceStone(self.app), event)
                self.assertIs(self.app.board.map[col][row], None)

    def test_col_row_custom(self):
        event = tk.Event()
        event.x = 5
        event.y = 5
        self.app.execute_command(PlaceStone(self.app), event)
        self.assertIs(self.app.board.map[0][0], None)

        event.x = self.app.board.board_size - 5
        event.y = self.app.board.board_size - 5
        self.app.execute_command(PlaceStone(self.app), event)
        self.assertIs(self.app.board.map[-1][-1], None)
'''


# default = [[Stone() for _ in range(19)] for _ in range(19)]


if __name__ == "__main__":
    unittest.main()

