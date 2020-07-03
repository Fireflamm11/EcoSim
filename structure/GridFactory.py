from implementation.agents.VillageAgent import VillageAgent
from implementation.places.FiniteFood import FiniteFood
from implementation.places.Tile import Tile
from implementation.pops.TestPop import TestPop
from implementation.settlements.Village import Village
from structure.Grid import Grid
from structure.places.Place import Place


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

        elif world_type == 'test_agriculture':
            # World config data
            num_settlements_per_tile = 1
            num_pops_per_settlement = 10
            # world generation
            for x in range(width):
                for y in range(height):
                    plc = Tile(grid, x, y)
                    grid.places[x].append(plc)
                    for i in range(num_settlements_per_tile):
                        vlg = Village(plc, num_pops_per_settlement)
                        vlg_ag = VillageAgent(vlg)
                        vlg.agents.append(vlg_ag)
                        plc.settlements.append(vlg)

        else:
            raise ValueError('no valid world type')

        return grid
