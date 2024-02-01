from abc import ABC, abstractmethod

class Command(ABC):
    """Command interface"""

    def __init__(self, board):
        self.board = board

    @abstractmethod
    def execute(self, event):
        pass


class PlaceStone(Command):
    """Board command for placing the stone"""

    def undo(self):
        self.board.map[self.row - 1][self.col - 1].destroy()
        self.board.map[self.row - 1][self.col - 1] = None

    def execute(self, event, stone_color):
        state = self.board.place_stone(event, stone_color)

        # is stone placed?
        if state is not None:
            # save row and column for undo
            self.row, self.col = state
            return True
        return False