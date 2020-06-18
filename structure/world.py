from structure.grid import Grid


class World:

    def __init__(self, height, width, world_type='empty'):
        self.type = world_type
        self.grid = Grid(self, height, width)

    def test_print(self):
        directions = ['nw', 'ne', 'e', 'se', 'sw', 'w']
        print('x-Coordinate')
        x = int(input())
        print('y-Coordinate')
        y = int(input())

        place = self.grid.places[x][y]

        for direction in directions:
            neighbor = place.get_neighbor(direction)
            print(neighbor.x, neighbor.y)
