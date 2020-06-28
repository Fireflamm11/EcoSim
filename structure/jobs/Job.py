from abc import ABC, abstractmethod


class Job(ABC):

    @classmethod
    @abstractmethod
    def work(cls, agent, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def get_resources(cls, agent, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def on_migration(cls, pop, **kwargs):
        pass
