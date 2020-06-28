from random import randint

import numpy as np

from structure.places.Place import Place


class Tile(Place):
    def __init__(self, grid, x, y):
        super().__init__(grid, x, y)
        self.soil_quality = randint(1, 2)
        self.arable_land = int(np.random.normal(100, 25))

        self.village_counter = 1

        counter = 0
        for settlement in self.settlements:
            counter += settlement.arable_land
        self.free_land = self.arable_land - counter
