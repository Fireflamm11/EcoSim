from implementation.places.FiniteFood import FiniteFood
from implementation.pops.TestPop import TestPop
from structure.Grid import Grid
from structure.Place import Place


class GridFactory:

    @classmethod
    def generate_places(cls, world, world_type, height, width):
        grid = Grid(world, height, width)
        if world_type == 'empty':
            for x in range(width):
                for y in range(height):
                    grid.places[x].append(Place(grid, x, y))
        elif world_type == 'test_food':
            for x in range(width):
                for y in range(height):
                    plc = FiniteFood(grid, x, y)
                    grid.places[x].append(plc)
                    plc.nomads.append(TestPop(plc))

        else:
            raise ValueError('no valid world type')

        return grid
