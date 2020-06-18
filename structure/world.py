from structure.grid import Grid

class World:
    def __init__(self, height, width):
        self.grid = Grid(self, height, width)
    
    def testprint(self):
        print("width of my grid: ", self.grid.width)