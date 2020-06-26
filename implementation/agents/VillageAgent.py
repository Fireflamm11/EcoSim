import importlib

import numpy as np

from structure.agents.Agent import Agent
from structure.agents.StrataAgent import StrataAgent
from structure.places.Place import Place


class VillageAgent(Agent, Place):

    def __init__(self, village, plc):
        super().__init__()
        self.path_settlements = 'implementation.agents.strata_agents.'
        self.village = village
        self.place = plc  # TODO Why does this know the place

        self.starving = []

        self._strata_agent: StrataAgent = self.update_strata()

    def step(self):
        self._strata_agent.work(self)
        self._strata_agent.consume(self)
        self._strata_agent.pop_development(self)
        self._strata_agent.settlement_development(self)

    def strata_agent(self):
        return self._strata_agent

    def update_strata(self):
        strata = self.village.strata
        try:
            path = self.path_settlements + strata + 'Agent'
            return getattr(importlib.import_module(path), strata + 'Agent')
        except NameError:
            raise NameError

    def kill_pop(self, pop):
        self.village.pops.remove(pop)
        if self.village.place.changed_values.get('dead') is not None:
            self.village.place.changed_values['dead'] += 1
        else:
            self.village.place.changed_values['dead'] = 1

    def kill_pops(self, pops):
        self.village.pops = [x for x in self.village.pops if x not in pops]
        self.village.place.grid.world.dead_pops.extend(pops)
        if self.village.place.changed_values.get('dead') is not None:
            self.village.place.changed_values['dead'] += len(pops)
        else:
            self.village.place.changed_values['dead'] = len(pops)

    def ageing(self):
        for pop in self.village.pops:
            pop.age += 1
            if pop.age >= 30:
                pop.health -= 10
            if pop.age >= 40:
                pop.health -= 10
            if pop.health <= 0:
                self.kill_pop(pop)

    def migrate_pops(self):
        if len(self.starving) == 0:
            return

        counter = 0
        indices = np.random.randint(low=0, high=len(self.starving), size=7)
        migrating = np.split(np.array(self.starving), indices)
        self.village.pops = [x for x in self.village.pops if
                             x not in self.starving]
        for direction, neighbor in self.village.place.get_neighbors().items():
            self.village.place.grid.grid_manager.migrating[neighbor].extend(
                migrating[counter])
            counter += 1
            # neighbor = self.village.place.neighbors[direction]
            # for settlement in neighbor.settlements:
            #     if settlement.arable_land - len(settlement.pops) > 0:
            #         settlement.pops.extend(self.starving)
            #         if settlement.place.changed_values.get('migrants'):
            #             settlement.place.changed_values['migrants'] += len(
            #                 self.starving)
            #         else:
            #             settlement.place.changed_values['migrants'] = len(
            #                 self.starving)
