class Place:

    def __init__(self, grid, x, y):
        self.grid = grid
        self.x = x
        self.y = y

        self.resources = []

        self.settlement = None
        self.nomads = []
