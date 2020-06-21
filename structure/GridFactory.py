from implementation.agents.VillageAgent import VillageAgent
from implementation.places.FiniteFood import FiniteFood
from implementation.places.Tile import Tile
from implementation.pops.TestPop import TestPop
from implementation.settlements.Village import Village
from structure.Grid import Grid
from structure.Place import Place
from structure.PopFactory import PopFactory


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
            food_need = 2
            # world generation
            for x in range(width):
                for y in range(height):
                    plc = Tile(grid, x, y)
                    grid.places[x].append(plc)
                    for i in range(num_settlements_per_tile):
                        vlg = Village(plc, "communal")
                        for j in range(num_pops_per_settlement):
                            PopFactory.generate_pops(vlg, food_need, "farmer")
                        vlg_ag = VillageAgent(vlg, plc)
                        vlg.agents.append(vlg_ag)
                        plc.settlements.append(vlg)

        else:
            raise ValueError('no valid world type')

        return grid
