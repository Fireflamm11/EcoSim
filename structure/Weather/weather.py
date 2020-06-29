from abc import ABC, abstractmethod


class Weather(ABC):

    @classmethod
    @abstractmethod
    def food_impact(cls, agent, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def climate_impact(cls, place, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def pop_impact(cls, pop, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def settlement_impact(cls, settlement, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def tile_impact(cls, place, **kwargs):
        pass



