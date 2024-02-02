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


class AlternateCommand(UICommand):
    """Side-menu button command for switching to alternate color mode for colorer"""

    def execute(self):
        self.app.stone_colorer.alternate = True


class ResetCommand(UICommand):
    """Clean up the board(, and command history)"""

    # TODO auto save the board, for restoring

    def execute(self):
        for r in range(len(self.app.board.map)):
            for c in range(len(self.app.board.map[r])):
                if self.app.board.map[r][c] is not None:
                    self.app.board.map[r][c].destroy()
                    self.app.board.map[r][c] = None
        
        # app history stores only active commands!
        self.app.history.reset()
        AlternateCommand(self.app).execute()
