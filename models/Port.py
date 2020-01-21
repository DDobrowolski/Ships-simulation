from models.Point import Point


class Port(Point):
    def __init__(self, pos, free_docks, containers_out, containers_in):
        super().__init__(pos)
        self._free_docks = free_docks
        self._containers_out = containers_out
        self._containers_in = containers_in
