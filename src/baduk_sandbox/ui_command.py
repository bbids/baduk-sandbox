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
