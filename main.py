import logging

from app import App
from mainframe import Mainframe
from board import Board
from side_menu import SideMenu


logging.basicConfig(level=logging.DEBUG)

root = App()
mainframe = Mainframe(root)
side_menu = SideMenu(mainframe)
board = Board(mainframe)

# logging.debug(board["height"])
root.mainloop()