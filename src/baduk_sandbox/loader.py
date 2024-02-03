import tkinter as tk

from .event import EventWrapper
from .action_command import PlaceStone

class Loader:

    def __init__(self, app, file_path):
        self._app = app
        self._file_path = file_path
        self._moves = []
        pass

    def read_moves(self):
        with open(self._file_path, "r", encoding="utf-8") as f:
            file_lines = f.readlines()


        for line in file_lines:
            if line[:2] == "(;":
                line = line[2:]
            elif line[0] == ";":
                line = line[1:]
            

            if line[:2] == "B[" or line[:2] == "W[":
                move_col = self.parse_move(line[2])
                move_row = self.parse_move(line[3])
                self.moves.append((move_col, move_row))

    def parse_move(self, char):
        # col: a = 1
        asc_col = ord(char)
        return asc_col - ord('a') + 1
    
    def play(self):
        """Buggy, because the game has no logic right now. """
        
        self._app.sound_off()
        for col, row in self.moves:
            event_w = EventWrapper(tk.Event())
            event_w.col = col
            event_w.row = row
            PlaceStone(self._app, event_w).execute()
        self._app.sound_on()    

    @property
    def moves(self):
        return self._moves


if __name__ == "__main__":
    game = Loader("../../game.sgf")
    game.read_moves()
    print(game.moves)
        
