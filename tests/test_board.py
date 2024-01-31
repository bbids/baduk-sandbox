import unittest
import tkinter as tk

from src.baduk_sandbox.main import start_app

#from tests.testBoard import TestBoard



class TestBoard(unittest.TestCase):

    """
    def _start_app(self):
        self.app.mainloop()
    """

    def setUp(self):
        self.app = start_app()
        # self._start_app()

    def tear_down(self):
        self.app.destroy()

    def test_col_row(self):
        event = tk.Event()
        event.x = 41
        event.y = 41

        # the events don't work have to do it manually
        # self.app.board.event_generate("<1>", event=event)
        self.app.board.on_board_click(event, "black")

        default[0][0] = "black"

        self.assertEqual(repr(self.app.board.map[0][0]), default[0][0])



default = [[None for _ in range(19)] for _ in range(19)]


if __name__ == "__main__":
    unittest.main()

