import logging

from src.app import App
from src.mainframe import Mainframe
from src.board import Board
from src.side_menu import SideMenu


logging.basicConfig(level=logging.DEBUG)

root = App()
mainframe = Mainframe(root)
side_menu = SideMenu(mainframe)
board = Board(mainframe)

# logging.debug(board["height"])
root.mainloop()