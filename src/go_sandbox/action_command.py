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

    def __init__(self, app, event_w):
        super().__init__(app)
        self._event_w = event_w

    def undo(self):
        self._app.board.remove_stone(self._event_w)

    def execute(self):
        success = self._app.board.place_stone(self._event_w)
        if success:
            self._app.history.push(self)


class RemoveStone(ActionCommand):
    """Remove the stones that have no liberties"""

    def __init__(self, app, event_w):
        super().__init__(app)
        self._event_w = event_w

    def undo(self):
        self._app.board.place_stone(self._event_w)

    def execute(self):
        success = self._app.board.remove_stone(self._event_w)
        if success:
            self._app.history.push(self)
