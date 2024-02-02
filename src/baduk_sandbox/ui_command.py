from abc import ABC, abstractmethod

class UICommand(ABC):
    """Command interface"""

    def __init__(self, app):
        self.app = app

    @abstractmethod
    def execute(self):
        pass


class BlackCommand(UICommand):
    """Side-menu command for switching stone placement colorer to mode black"""

    def execute(self):
        self.app.stone_colorer.alternate = False
        self.app.stone_colorer.color = "black"
    
class WhiteCommand(UICommand):
    """Side-menu command for switching stone placement colorer to mode white"""

    def execute(self):
        self.app.stone_colorer.alternate = False
        self.app.stone_colorer.color = "white"

class ResetCommand(UICommand):
    """Clean up the board(, and command history)"""
    # TODO auto save the board, for restoring

    def execute(self):
        for r in range(len(self.app.board.map)):
            for c in range(len(self.app.board.map[r])):
                if self.app.board.map[r][c] is not None:
                    self.app.board.map[r][c].destroy()
                    self.app.board.map[r][c] = None
        self.app.history.reset()
        self.app.stone_colorer.alternate = True
        self.app.stone_colorer.color = "black"
