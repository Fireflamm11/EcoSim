from structure.GridFactory import GridFactory


class World:

    def __init__(self, height, width, world_type='empty', start_date=0):
        self.time = start_date
        self.type = world_type
        self.grid = GridFactory.generate_places(self, self.type, height, width)

    def step(self):
        self.time += 1
        self.grid.step()
