from models.Point import Point
from helpers.Vector2 import Vector2
from pygame import time
import csv
from random import randint


class Ship(Point):
    available_ports = []

    def __init__(self, name, pos, destination, port, owner, capacity, max_fuel, current_fuel, condition,  available_destinations=[]):
        super().__init__(pos, name)
        self._port = port
        self._owner = owner
        self._capacity = capacity
        self._max_fuel = max_fuel
        self._current_fuel = current_fuel
        self._condition = condition
        self._heading = Vector2()
        self._destination = destination
        self._clock = time.Clock()
        self._speed = 200
        self._available_destinations = available_destinations
        self._delay = 0

    def move(self):
        self._heading = Vector2.from_points(
            self.position, self._destination.position)
        self._heading.normalize()

    def update(self):
        time_passed = self._clock.tick()
        time_passed_seconds = time_passed / 1000.0
        distance_moved = time_passed_seconds * self._speed
        if not self._is_at_destination():
            self._position += self._heading * distance_moved
        else:
            if self._destination.free_docks > 0:
                pass
                # containers logic...
            if self._delay == 0:
                self._dock()
            elif (time.get_ticks() / 1000 - self._delay) >= 5:
                self._sail_out()

    def _dock(self):
        self._destination.free_docks -= 1
        self._delay = time.get_ticks() / 1000
        print(f"{self.name} is docking...", self._destination.name, 'free docks: ',
              self._destination.free_docks)

    def _sail_out(self):
        self._delay = 0
        self._destination.free_docks += 1
        print(f"{self.name} is sailing out...", self._destination.name, 'free docks: ',
              self._destination.free_docks)
        self._generate_new_destination()
        self.move()

    def _is_at_destination(self):
        return self._position.get_distance_to(self._destination.position) <= 2

    def _generate_new_destination(self):
        max_index = len(self._available_destinations)-1
        new_index = randint(0, max_index)
        self._destination = self._available_destinations[new_index]
