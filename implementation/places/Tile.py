from random import randint
from implementation.weathers.AverageWeather import AverageWeather
from implementation.weathers.Warm_Summer import WarmSummerWeather
from implementation.weathers.Stormy import StormyWeather


import numpy as np

from structure.places.Place import Place


class Tile(Place):
    def __init__(self, grid, x, y):
        super().__init__(grid, x, y)
        self.soil_quality = randint(1, 2)
        self.arable_land = int(np.random.normal(100, 25))

        self.village_counter = 1

        self.free_land = int(self.arable_land)

        self.weathers = [AverageWeather, WarmSummerWeather, StormyWeather]
        self.weather = None
        self.weather_probability = dict.fromkeys(self.weathers)
        self.standard_probability = [0.7, 0.2, 0.1]
        for weather in self.weather_probability:
            self.weather_probability[weather] = self.standard_probability
# missing: changabel? maybe redundant


    def step(self):
        self.set_weather()
        print(self.weather)
        super().step()

    def set_weather(self):
        idx = np.random.choice(3, p=self.standard_probability)
        self.weather = self.weathers[idx]



