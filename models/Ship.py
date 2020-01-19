from models.Point import Point


class Ship(Point):
    def __init__(self, port, owner, capacity, max_fuel, current_fuel, condition):
        super().__init__()
        self._port = port
        self._owner = owner
        self._capacity = capacity
        self._max_fuel = max_fuel
        self._current_fuel = current_fuel
        self._condition = condition
        self._rendered = None

    def move(self, destination):
        if self._position[0] == destination['x'] and self._position[1] == destination['y']:
            return True
        elif self._position[0] < destination['x']:
            if self._position[1] == destination['y']:
                source.move_ip(10, 0)
            elif self._position[1] < destination['y']:
                source.move_ip(10, 10)
            elif self._position[1] > destination['y']:
                source.move_ip(10, -10)
        elif self._position[0] > destination['x']:
            if self._position[1] == destination['y']:
                source.move_ip(-10, 0)
            elif self._position[1] < destination['y']:
                source.move_ip(-10, 10)
            elif self._position[1] > destination['y']:
                source.move_ip(-10, -10)
        elif self._position[1] < destination['y']:
            if self._position[0] == destination['x']:
                source.move_ip(0, 10)
            elif self._position[0] < destination['x']:
                source.move_ip(10, 10)
            elif self._position[0] > destination['x']:
                source.move_ip(-10, 10)
        elif self._position[1] > destination['y']:
            if self._position[0] == destination['x']:
                source.move_ip(0, -10)
            elif self._position[0] < destination['x']:
                source.move_ip(10, -10)
            elif self._position[0] > destination['x']:
                source.move_ip(-10, -10)
        return False
