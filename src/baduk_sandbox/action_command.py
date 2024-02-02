from abc import ABC, abstractmethod


class ActionCommand(ABC):
    """Command interface"""

    def __init__(self, app):
        self._app = app

    @abstractmethod
    def execute(self):
        pass


class PlaceStone(ActionCommand):
    """Board command for placing the stone"""

    def __init__(self, app, event):
        super().__init__(app)
        self._event = event

    def undo(self):
        self._app.board.remove_stone(self._event.x, self._event.y)

    def execute(self):
        success = self._app.board.place_stone(self._event)
        if success:
            self._app.history.push(self)

'''
class RemoveStone(ActionCommand):
    """Remove the stones that have no liberties"""

    def __init__(self, app, event):
        super().__init__(app)
        self._event = event

    def undo(self):
        # PlaceStone(self._app, self._event).execute()

    def execute(self):
        print("X: ", self._event.x, "Y: ", self._event.y)
        """
        success = self._app.board.remove_stone(self._event.x, self._event.y)
        if success:
            self._app.history.push(self)
        """
'''
