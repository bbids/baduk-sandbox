class EventWrapper():
    """Wrapper for event, for extra properties"""

    def __init__(self, event):
        self._event = event
        self.row = None
        self.col = None

    @property
    def event(self):
        return self._event

    @property
    def row(self):
        return self._row
    
    @row.setter
    def row(self, value):
        self._row = value
    
    @property
    def col(self):
        return self._col
    
    @col.setter
    def col(self, value):
        self._col = value