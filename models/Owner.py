import pygame


class Owner:
    cash_event = pygame.event.Event(pygame.USEREVENT, val='cash_modified')

    def __init__(self, name, init_cash):
        self._name = name
        self._cash = init_cash

    def to_dict(self):
        return {'nazwa': self.name, 'srodki': self._cash}

    @property
    def name(self):
        return self._name

    @property
    def cash(self):
        return self._cash

    def add_cash(self, cash):
        pygame.event.post(Owner.cash_event)
        self._cash += cash

    def remove_cash(self, cash):
        pygame.event.post(Owner.cash_event)
        self._cash -= cash
