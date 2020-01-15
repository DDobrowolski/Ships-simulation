class Ship:
    def __init__(self, port, position, capacity, max_fuel, current_fuel, condition):
        self.position = position
        self.port = port
        self.capacity = capacity
        self.max_fuel = max_fuel
        self.current_fuel = current_fuel
        self.condition = condition

    