import logging

class PlayMode:
    """Represents the configuration options for the game"""

    def __init__(self, app, alternate=True, initial_color="black"):
        self.alternate = alternate
        self.color = initial_color
        self._app = app

    def game_start(self):
        self.alternate = True
        self.color = "black"

        alt_btn = self._app.side_menu.alternate_btn
        self._app.side_menu.set_active(alt_btn)

    def black_only(self):
        self.alternate = False
        self.color = "black"

    def white_only(self):
        self.alternate = False
        self.color = "white"

    def alternate_stones(self):
        self.alternate = True

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
        if value  in ("black", "white"):
            self._color = value
        else:
            logging.debug("play mode color not black/white")

    @property
    def alternate(self):
        return self._alternate

    @alternate.setter
    def alternate(self, value):
        if isinstance(value, bool):
            self._alternate = value
        else:
            logging.debug("play mode alternate not boolean value")
