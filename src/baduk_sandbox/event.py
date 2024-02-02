class EventWrapper():
    """Wrapper for event, for extra properties"""

    def __init__(self, event):
        self.event = event
        self.row = None
        self.col = None