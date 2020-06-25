from abc import ABC, abstractmethod

from structure.agents.Agent import Agent


class StrataAgent(ABC, Agent):

    @classmethod
    @abstractmethod
    def work(cls, agent, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def consume(cls, agent, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def pop_development(cls, agent, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def settlement_development(cls, agent, **kwargs):
        pass
