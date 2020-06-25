import numpy as np

from structure.PopFactory import PopFactory
from structure.Settlement import Settlement


class Village(Settlement):
    def __init__(self, place, start_pops, strata):
        super().__init__(place)
        self.strata = strata
        self.arable_land = np.random.random() * 100 + 10

        for idx in range(start_pops):
            PopFactory.generate_pops(self, 2, "farmer")
