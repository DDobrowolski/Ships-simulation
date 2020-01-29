from models.Point import Point


class Port(Point):
    def __init__(self, pos, name, free_docks, containers_out, containers_in=[]):
        super().__init__(pos, name)
        self._free_docks = free_docks
        self._containers_out = containers_out
        self._containers_in = containers_in

    def to_dict(self):
        return {'nazwa': self.name, 'kontenery_wejscie': len(self._containers_in), 'kontenery_wyjscie': len(self._containers_out)}

    @property
    def free_docks(self):
        return self._free_docks

    @free_docks.setter
    def free_docks(self, free_docks):
        self._free_docks = free_docks

    @property
    def containers_out(self):
        return self._containers_out

    @containers_out.setter
    def containers_out(self, containers_out):
        self._containers_out = containers_out

    @property
    def containers_in(self):
        return self._containers_in

    def _remove_specific_containers_out(self, containers):
        self._containers_out = [
            c for c in self._containers_out if c.destination_port not in containers]

    def get_specific_containers_out(self, destination, quantity):
        output = []
        for index, cont in enumerate(self._containers_out):
            output.append(
                cont) if index < quantity and cont.destination_port is destination else None
        self._remove_specific_containers_out(output)
        return output

    def add_specific_containers_in(self, containers):
        self._containers_in += containers
