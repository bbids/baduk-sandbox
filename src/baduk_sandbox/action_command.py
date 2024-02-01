from abc import ABC, abstractmethod

class ActionCommand(ABC):
    """Command interface"""

    def __init__(self, app):
        self.app = app
        self.board = app.board

    @abstractmethod
    def execute(self):
        pass


class PlaceStone(ActionCommand):
    """Board command for placing the stone"""

    def undo(self):
        assert hasattr(self, "row") and hasattr(self, "col")
        self.board.map[self.row - 1][self.col - 1].destroy()
        self.board.map[self.row - 1][self.col - 1] = None

    def execute(self, event):
        stone_color = self.app.stone_colorer.color
        state = self.board.place_stone(event, stone_color)

        # is stone placed?
        if state is not None:
            # save row and column for undo
            self.row, self.col = state
