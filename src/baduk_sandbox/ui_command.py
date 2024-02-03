from abc import ABC, abstractmethod
from .loader import Loader


class UICommand(ABC):
    """Command interface"""

    def __init__(self, app):
        self._app = app

    @abstractmethod
    def execute(self):
        pass


class BlackCommand(UICommand):
    """Side-menu command for switching stone placement colorer to mode black"""

    def execute(self):
        self._app.play_mode.black_only()


class WhiteCommand(UICommand):
    """Side-menu command for switching stone placement colorer to mode white"""

    def execute(self):
        self._app.play_mode.white_only()


class AlternateCommand(UICommand):
    """Side-menu button command for switching to alternate color mode for colorer"""

    def execute(self):
        self._app.play_mode.alternate_stones()


class ResetCommand(UICommand):
    """Clean up the board(, and command history)"""

    # TODO auto save the board, for restoring

    def execute(self):
        self._app.board.clear()
        self._app.history.reset()
        self._app.play_mode.game_start()


class LoadCommand(UICommand):
    """Load the sgf file command"""

    def __init__(self, app, file_path):
        super().__init__(app)
        self._file_path = file_path

    def execute(self):
        game = Loader(self._app, self._file_path)
        game.read_moves()
        ResetCommand(self._app).execute()
        game.play()
