from models.Point import Point
from helpers.Vector2 import Vector2
from pygame import time


class Ship(Point):
    def __init__(self, pos, destination, port, owner, capacity, max_fuel, current_fuel, condition):
        super().__init__(pos)
        self._port = port
        self._owner = owner
        self._capacity = capacity
        self._max_fuel = max_fuel
        self._current_fuel = current_fuel
        self._condition = condition
        self._heading = Vector2()
        self._destination = Vector2(destination)
        self._clock = time.Clock()
        self._speed = 250

    def move(self):
        self._heading = Vector2.from_points(self.position, self._destination)
        self._heading.normalize()

    def update(self):
        time_passed = self._clock.tick()
        time_passed_seconds = time_passed / 1000.0
        distance_moved = time_passed_seconds * self._speed
        if(float(round(self.position[0])) != self._destination.get_x() or float(round(self.position[1])) != self._destination.get_y()):
            self._position += self._heading * distance_moved
