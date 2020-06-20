from threading import Thread

from structure.GridFactory import GridFactory
import time


class World:

    def __init__(self, height, width, world_type='empty', start_date=0):
        self.date = start_date
        self.type = world_type
        self.grid = GridFactory.generate_places(self, self.type, height, width)

        self.dead_pops = []

    def step(self):
        self.date += 1
        self.grid.step()
