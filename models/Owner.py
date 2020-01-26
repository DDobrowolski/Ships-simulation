class Owner:
    def __init__(self, name, init_cash):
        self._name = name
        self._cash = init_cash

    @property
    def name(self):
        return self._name

    @property
    def cash(self):
        return self._cash

    def add_cash(self, cash):
        self._cash += cash

    def remove_cash(self, cash):
        self._cash -= cash
