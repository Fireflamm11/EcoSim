class Place:

    def __init__(self, grid, x, y):
        self.observers = []
        self.changed_values = {}

        self.grid = grid
        self.x = x
        self.y = y

        self.resources = {}

        self.settlements = []
        self.nomads = []

    def step(self):
        for nmd in self.nomads:
            nmd.step()
        for stl in self.settlements:
            stl.step()
        if self.changed_values:
            self.notify_observer()
        self.changed_values.clear()

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observer(self):
        for obs in self.observers:
            obs.notify(self.changed_values)

    def get_neighbor(self, direction):
        # We have to differ between the rows on how to determine northern and
        # southern neighbors. For this we have to check, if the row number is
        # odd or even and subtract the modulo 2 of the row index
        try:
            if direction == 'nw':
                return self.grid.places[self.x - 1 + (self.y % 2)][self.y - 1]
            elif direction == 'ne':
                return self.grid.places[self.x + (self.y % 2)][self.y - 1]
            elif direction == 'e':
                return self.grid.places[self.x + 1][self.y]
            elif direction == 'se':
                return self.grid.places[self.x + (self.y % 2)][self.y + 1]
            elif direction == 'sw':
                return self.grid.places[self.x - 1 + (self.y % 2)][self.y + 1]
            elif direction == 'w':
                return self.grid.places[self.x - 1][self.y]
            else:
                raise ValueError(direction + ' Invalid direction for getting '
                                             'neighbor of place')
        except IndexError:
            if direction == 'ne':
                return self.grid.places[0][self.y - 1]
            elif direction == 'e':
                return self.grid.places[0][self.y]
            elif direction == 'se':
                x = self.x + (self.y % 2)
                y = self.y + 1
                if self.x + (self.y % 2) not in range(len(self.grid.places)):
                    x = 0
                if self.y + 1 not in range(len(self.grid.places[x])):
                    y = 0
                return self.grid.places[x][y]
            elif direction == 'sw':
                return self.grid.places[self.x - 1 + (self.y % 2)][0]
