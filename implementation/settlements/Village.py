import numpy as np


from structure.Settlement import Settlement


class Village(Settlement):
    def __init__(self, place, strata):
        super().__init__(place)
        self.strata = strata
        self.arable_land = np.random.random() * 10000 + 10
