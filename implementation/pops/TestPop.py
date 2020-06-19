import numpy as np


class TestPop:

    def __init__(self, place):
        self.place = place
        self.food_consumption = 1
        self.counter = 0

    def step(self):
        food = self.place.resources['food']
        if food >= self.food_consumption:
            new_food = food - self.food_consumption
            self.place.resources['food'] = new_food
            self.food_consumption += np.random.normal(0.2, 0.1)
        else:
            self.food_consumption -= np.random.normal(0.4, 0.1)
            self.place.changed_values['starving'] = True

        self.counter += 1
