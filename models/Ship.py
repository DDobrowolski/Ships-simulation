from models.Point import Point
from helpers.Vector2 import Vector2
from pygame import time
import csv
from random import randint


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
        if not self._is_at_destination():
            self._position += self._heading * distance_moved
        else:
            self._generate_new_destination()
            self.move()

    def _is_at_destination(self):
        return self._position.get_distance_to(self._destination) < 5

    def _generate_new_destination(self):
        with open('const/ports.csv') as csv_file:
            reader = list(csv.reader(csv_file, delimiter=','))
            max_index = len(reader)-1
            new_index = randint(1, max_index)
            self._destination = Vector2(
                (reader[new_index][1], reader[new_index][2]))
