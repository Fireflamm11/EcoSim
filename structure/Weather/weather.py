from abc import ABC, abstractmethod


class Weather(ABC):


    @classmethod
    @abstractmethod
    def pop_impact(cls, pop, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def tile_impact(cls, place, **kwargs):
        pass



