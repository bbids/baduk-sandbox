

class StonePlacement:
    """Represents the stone placmenet/color"""

    def __init__(self, alternate = True, initial_color = "black"):
        self.alternate = alternate
        self.color = initial_color

    def toggle_color(self):
        """Switch color if alternate is true"""
        if self.alternate:
            match self.color:
                case "black":
                    self.color = "white"
                case "white":
                    self.color = "black"

    def toggle_alternate(self):
        """Switch alternate"""
        match self.alternate:
            case True:
                self.alternate = False
            case False:
                self.alternate = True

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        assert value in  ("black", "white")
        self._color = value

    @property
    def alternate(self):
        return self._alternate

    @alternate.setter
    def alternate(self, value):
        assert isinstance(value, bool)
        self._alternate = value
