class CommandHistory:
    """Represents the history of commands"""

    def __init__(self):
        self._history = []

    def push(self, command):
        self.history.append(command)

    def pop(self):
        return self.history.pop()

    def size(self):
        return len(self.history)

    def reset(self):
        self._history = []

    @property
    def history(self):
        return self._history


"""
    history = []

    @staticmethod
    def push(command):
        CommandHistory.history.append(command)

    @staticmethod
    def pop():
        assert len(CommandHistory.history) > 0

        logging.debug(CommandHistory.history)
        return CommandHistory.history.pop()
    
    @staticmethod
    def get_history_size():
        return len(CommandHistory.history)
"""
