class Ship:
    def __init__(self, port, position, capacity, max_fuel, current_fuel, condition):
        self._position = position
        self._port = port
        self._capacity = capacity
        self._max_fuel = max_fuel
        self._current_fuel = current_fuel
        self._condition = condition

    