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
            if self.counter % 50 == 0:
                print('######################################################')
                print('Step:' + str(self.counter))
                print('######################################################')
                print('Pop on ' + str(self.place.x) + ', ' + str(
                    self.place.y) + ' consumed '
                      + str(self.food_consumption))
                print('Remaining food: ' + str(new_food))
            self.place.resources['food'] = new_food
            self.food_consumption += np.random.normal(0.2, 0.1)
        else:
            print('######################################################')
            print('Step:' + str(self.counter))
            print('######################################################')
            print('Pop starving on ' + str(self.place.x) + ', ' + str(
                self.place.y))
            print('Food remaining ' + str(self.place.resources['food']) +
                  ', Food consumed: ' + str(self.food_consumption))
            self.food_consumption -= np.random.normal(0.4, 0.1)

        self.counter += 1
