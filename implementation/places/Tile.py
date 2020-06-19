from structure.Place import Place
from random import randint


class Tile(Place):
    def __init__(self, grid, x, y):
        super().__init__(grid, x, y)
        self.soil_quality = randint(1, 2)
