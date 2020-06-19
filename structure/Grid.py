# gegenüberliegende Ränder sollen verbunden sein
# die Felder sind inhaltsleer, sind enthalten bloß einen place


class Grid:
    def __init__(self, world, height, width):
        self.world = world
        self.height = height
        self.width = width

        self.places = []

        for x in range(self.width):
            self.places.append([])

    def step(self):
        for col in self.places:
            for plc in col:
                plc.step()
