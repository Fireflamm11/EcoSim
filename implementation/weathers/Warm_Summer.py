from structure.Weather.weather import Weather


class WarmSummerWeather(Weather):

    @classmethod
    def pop_impact(cls, pop, **kwargs):
        pass

    @classmethod
    def tile_impact(cls, place, **kwargs):
        place.weather_impact = 1.5
