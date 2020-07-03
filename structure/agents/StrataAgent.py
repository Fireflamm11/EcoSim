from abc import ABC, abstractmethod

from structure.agents.Agent import Agent


class StrataAgent(ABC, Agent):
    """
    This agents encapsulates the behaviour for different strata. It does this
    by providing hook-Methods for central actions in the course of a step,
    which should be overridden by strata-Implementations. This class and its
    subclasses are designed to be used as container for methods and should not
    be initialised. Instead all methods are class-Methods, which are provided
    with the village-agent.

    """

    @classmethod
    @abstractmethod
    def job_redistribution(cls, agent, **kwargs):
        pass

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
