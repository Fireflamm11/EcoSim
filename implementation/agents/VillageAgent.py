import importlib
from random import shuffle

import numpy as np

from structure.agents.Agent import Agent
from structure.agents.StrataAgent import StrataAgent
from structure.places.Place import Place


class VillageAgent(Agent, Place):

    def __init__(self, village):
        super().__init__()
        self.path_strata_agents = 'implementation.agents.strata_agents.'
        self.village = village

        # self.starving = 0
        self.food_production_modifier = float(self.village.place.soil_quality) * float(self.village.place.weather_impact)
        self.light_starving = dict.fromkeys(self.village.job_types)
        self.heavy_starving = dict.fromkeys(self.village.job_types)

        self._strata_agent: StrataAgent = self.update_strata()

    def step(self):
        self._strata_agent.job_redistribution(self)

        self._strata_agent.work(self)
        self._strata_agent.consume(self)

        self._strata_agent.pop_development(self)
        self._strata_agent.settlement_development(self)
        """self.starving = 0"""

    def strata_agent(self):
        return self._strata_agent

    def update_strata(self):
        strata = self.village.strata
        try:
            path = self.path_strata_agents + strata + 'Agent'
            return getattr(importlib.import_module(path), strata + 'Agent')
        except NameError:
            raise NameError

    def kill_pop(self, pop):
        pop.on_death()
        if self.village.place.changed_values.get('dead') is not None:
            self.village.place.changed_values['dead'] += 1
        else:
            self.village.place.changed_values['dead'] = 1

    def kill_pops(self, pops):
        [pop.on_death() for pop in pops]
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


""" def migrate_pops(self):
        if self.starving <= 0:
            return

        moving_idx = np.random.default_rng().choice(len(self.village.pops),
                                                    size=int(self.starving),
                                                    replace=False)
        moving_pops = [self.village.pops[idx] for idx in moving_idx]
        counter = 0

        if len(moving_idx) < 6:
            indices = np.sort(
                np.random.default_rng().choice(6, size=6, replace=False))
        else:
            indices = np.sort(
                np.random.default_rng().choice(len(moving_idx), size=6,
                                               replace=False))

        migrating = np.split(np.array(moving_pops), indices)
        shuffle(migrating)
        # self.village.pops = [x for x in self.village.pops if
        #                      x not in moving_pops]

        for direction, neighbor in self.village.place.get_neighbors().items():
            self.village.place.grid.grid_manager.migrating[neighbor].extend(
                migrating[counter])
            counter += 1
"""