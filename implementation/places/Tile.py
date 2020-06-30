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
        self.weather_probability = [0.7, 0.2, 0.1]
        self.weather_impact = 1
        self.food_production_modifier = self.soil_quality * self.weather_impact

    def step(self):
        self.set_weather()
        self.weather.tile_impact(self)
        super().step()

    def set_weather(self):
        idx = np.random.choice(3, p=self.weather_probability)
        self.weather = self.weathers[idx]



