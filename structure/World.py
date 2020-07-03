from structure.GridFactory import GridFactory
from structure.GridManager import GridManager


class World:

    def __init__(self, height, width, world_type='empty', start_date=0):
        self.date = start_date
        self.type = world_type
        self.grid = GridFactory.generate_places(self, self.type, height, width)
        self.grid.grid_manager = GridManager(self.grid)

        self.dead_pops = []

    def step(self):
        self.date += 1
        self.grid.step()
