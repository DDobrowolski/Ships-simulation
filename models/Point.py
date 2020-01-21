from helpers.Vector2 import Vector2


class Point:
    def __init__(self, position, name='Point'):
        self._name = name
        self._position = Vector2(position)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = Vector2(position)

    @property
    def name(self):
        return self._name
