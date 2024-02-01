

class StonePlacement:
    """Represents the stone placmenet/color"""

    def __init__(self, alternate = True, initial_color = "black"):
        self.alternate = alternate
        self.color = initial_color

    def toggle_color(self):
        if self.alternate:
            match self.color:
                case "black":
                    self.color = "white"
                case "white":
                    self.color = "black"

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value