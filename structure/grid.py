# gegenüberliegende Ränder sollen verbunden sein
# die Felder sind inhaltsleer, sind enthalten bloß einen place


class Grid:
    def __init__(self, world, height, width):
        self.world = world
        self.height = height
        self.width = width