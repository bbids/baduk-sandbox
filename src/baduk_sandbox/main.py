import logging

from .app import App

def start_app() -> App:
    logging.basicConfig(level=logging.DEBUG)
    root = App()
    return root