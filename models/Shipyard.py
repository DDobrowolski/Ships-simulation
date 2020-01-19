from models.Point import Point


class Shipyard(Point):
    def __init__(self, free_docks):
        super().__init__()
        self._free_docks = free_docks
