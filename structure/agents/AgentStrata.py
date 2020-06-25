from abc import ABC, abstractmethod

from structure.agents.Agent import Agent


class AgentStrata(ABC, Agent):

    @classmethod
    @abstractmethod
    def production(cls, agent, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def supply(cls, agent, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def pop_development(cls, agent, **kwargs):
        pass
