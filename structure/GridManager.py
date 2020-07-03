class GridManager:

    def __init__(self, grid):
        self.grid = grid

        # migration[destination_place] = pops
        self.migrating = {}
        for x in self.grid.places:
            for place in x:
                self.migrating[place] = []

    def step(self):
        self.migration()

    def migration(self):
        for place, pops in self.migrating.items():
            place.migration(pops)
            if place.changed_values.get('migrants'):
                place.changed_values['migrants'] += len(pops)
            else:
                place.changed_values['migrants'] = len(pops)

            self.migrating[place] = []
