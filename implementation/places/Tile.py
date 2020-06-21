from random import randint

import numpy as np

from structure.Place import Place


class Tile(Place):
    def __init__(self, grid, x, y):
        super().__init__(grid, x, y)
        self.soil_quality = randint(1, 2)
        self.arable_land = int(np.random.normal(100, 25))
        self.free_land = range(0, self.arable_land)
