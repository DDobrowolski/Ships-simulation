from models.Point import Point
from helpers.Vector2 import Vector2
from pygame import time
import csv
from random import randint


class Ship(Point):

    def __init__(self, name, pos, destination, available_destinations=[], owner=None, port=None, capacity=5000, condition=100, max_fuel=100, current_fuel=100):
        super().__init__(pos, name)
        self._port = port
        self._owner = owner
        self._capacity = capacity
        self._containers = []
        self._max_fuel = max_fuel
        self._current_fuel = current_fuel
        self._condition = condition
        self._heading = Vector2()
        self._destination = destination
        self._clock = time.Clock()
        self._speed = 100
        self._available_destinations = available_destinations
        self._delay = 0
        self._move_interval = time.get_ticks() / 1000

    def to_dict(self):
        return {
            'nazwa': self.name,
            'pozycja': self.position.as_tuple(),
            'kontenery': len(self._containers),
            'armator': self._owner.name,
            'paliwo': f"{self._current_fuel}/{self._max_fuel}",
            'stan': f"{self._condition}/100%",
            'cel': self._destination.name
        }

    def to_string(self):
        return f"nazwa: {self.name},<br/>kontenery: {len(self._containers)},<br/>armator: {self._owner.name},<br/>paliwo: {self._current_fuel}/{self._max_fuel},<br/>stan: {self._condition}/100%,<br/>cel: {self._destination.name}"

    def move(self):
        self._heading = Vector2.from_points(
            self.position, self._destination.position)
        self._heading.normalize()

    def update(self):
        time_passed = self._clock.tick()
        time_passed_seconds = time_passed / 1000.0
        distance_moved = time_passed_seconds * self._speed
        if not self._is_at_destination():
            self._sail(distance_moved)
        else:
            if self._destination.free_docks == 0:
                self._sail_out()
                return
            if self._delay == 0:
                self._dock()
                self._unload_containers()
            elif (time.get_ticks() / 1000 - self._delay) >= 5:
                self._sail_out()

    def _sail(self, distance_moved):
        self._position += self._heading * distance_moved
        if self._move_interval != 0 and (time.get_ticks() / 1000 - self._move_interval) % 1 == 0:
            self._current_fuel -= round(len(self._containers)*0.005)
            self._condition -= round(len(self._containers)*0.002)
            print(self.name, 'fuel:', self._current_fuel,
                  'condition:', self._condition, '%')

    def _unload_containers(self):
        containers_to_unload = [
            c for c in self._containers if c.destination_port is self._destination]
        # Adding cash to owner
        self._owner.add_cash(len(containers_to_unload) * 10)
        self._destination.add_specific_containers_in(containers_to_unload)
        self._containers = [
            c for c in self._containers if c.destination_port is not self._destination]
        # Generating new destination ports
        if len(self._destination.containers_out) == 0:
            self._destination.containers_out = self._destination.containers_in or []

    def _load_containers(self, destination):
        containers_to_load = self._destination.get_specific_containers_out(
            destination, self._capacity - len(self._containers))
        self._containers += containers_to_load
        self._owner.remove_cash(len(containers_to_load) * 10)

    def _dock(self):
        self._destination.free_docks -= 1
        self._delay = time.get_ticks() / 1000
        self._move_interval = 0
        print(f"{self.name} is docking...", self._destination.name, 'free docks: ',
              self._destination.free_docks)

    def _sail_out(self):
        self._delay = 0
        self._move_interval = time.get_ticks() / 1000
        self._destination.free_docks += 1
        self._repair_and_tank()
        print(f"{self.name} is sailing out...", self._destination.name, 'free docks: ',
              self._destination.free_docks)

        self._generate_new_destination()
        self._load_containers(self._destination)
        print(self._name, 'containers count after loading:', len(self._containers))

        self.move()

    def _repair_and_tank(self):
        fuel_to_tank = self._max_fuel - self._current_fuel
        condition_percentage_to_repair = 100 - self._condition
        cash_to_remove = fuel_to_tank*1000 + condition_percentage_to_repair*3000
        self._owner.remove_cash(cash_to_remove)
        self._current_fuel = self._max_fuel
        self._condition = 100

    def _is_at_destination(self):
        return self._position.get_distance_to(self._destination.position) <= 2

    def _generate_new_destination(self):
        max_index = len(self._available_destinations)-1
        new_index = randint(0, max_index)
        self._destination = self._available_destinations[new_index]
