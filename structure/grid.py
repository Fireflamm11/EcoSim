# gegenüberliegende Ränder sollen verbunden sein
# die Felder sind inhaltsleer, sind enthalten bloß einen place
from structure.place import Place


class Grid:
    def __init__(self, world, height, width):
        self.world = world
        self.height = height
        self.width = width

        self.places = []

        for x in range(self.width):
            self.places.append([])

        self.generate_places()

    def generate_places(self):
        if self.world.type == 'empty':
            for x in range(self.width):
                for y in range(self.height):
                    self.places[x].append(Place(self, x, y))
        else:
            raise ValueError('no valid world type')
