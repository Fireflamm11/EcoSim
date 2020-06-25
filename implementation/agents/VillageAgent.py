import importlib

from structure.agents.Agent import Agent
from structure.agents.StrataAgent import StrataAgent
from structure.places.Place import Place


class VillageAgent(Agent, Place):

    def __init__(self, village, plc):
        super().__init__()
        self.path_settlements = 'implementation.agents.strata_agents.'
        self.village = village
        self.place = plc

        self.starving = 0

        self._strata_agent: StrataAgent = self.update_strata()

    def step(self):
        self._strata_agent.work(self)
        self._strata_agent.consume(self)
        self._strata_agent.pop_development(self)

    def strata_agent(self):
        return self._strata_agent

    def update_strata(self):
        strata = self.village.strata
        try:
            path = self.path_settlements + strata + 'Agent'
            return getattr(importlib.import_module(path), strata + 'Agent')
        except NameError:
            raise NameError
