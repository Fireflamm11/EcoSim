from structure.places.Place import Place


class FiniteFood(Place):

    def __init__(self, grid, x, y):
        super().__init__(grid, x, y)
        self.resources = {'food': 100}
