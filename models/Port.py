from models.Point import Point


class Port(Point):
    def __init__(self, pos, name, free_docks, containers_out, containers_in):
        super().__init__(pos, name)
        self._free_docks = free_docks
        self._containers_out = containers_out
        self._containers_in = containers_in

    @property
    def free_docks(self):
        return self._free_docks

    @free_docks.setter
    def free_docks(self, free_docks):
        self._free_docks = free_docks
