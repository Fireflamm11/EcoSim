import importlib

from structure.agents.Agent import Agent
from structure.agents.AgentStrata import AgentStrata
from structure.places.Place import Place


class VillageAgent(Agent, Place):

    def __init__(self, village, plc):
        super().__init__()
        self.path_settlements = 'implementation.settlements.'
        self.village = village
        self.place = plc

        self.starving = 0

        self.strata_agent: AgentStrata = self.update_strata()

    def step(self):
        self.strata_agent.production(self)
        self.strata_agent.supply(self)
        self.strata_agent.pop_development(self)

    def update_strata(self):
        strata = self.village.strata
        try:
            path = self.path_settlements + strata
            return getattr(importlib.import_module(path), strata)
        except NameError:
            raise NameError
