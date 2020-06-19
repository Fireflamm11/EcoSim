import numpy as np

from implementation.goods.Food import Food
from structure.Agent import Agent
from structure.Pop import Pop


class VillageAgent(Agent):
    def __init__(self, village):
        super().__init__()
        self.village = village

    def step(self):
        self.farm()
        self.eat()

    def farm(self):
        for pop in self.village.pops:
            for i in range(self.village.place.soil_quality):
                food = Food()
                try:
                    pop.inventory["food"].append(food)
                except KeyError:
                    pop.inventory["food"] = []
                    pop.inventory["food"].append(food)

    def eat(self):
        for pop in self.village.pops:
            try:
                if len(pop.inventory['food']) >= pop.food_need:
                    pop.inventory["food"] = pop.inventory["food"][
                                            :-pop.food_need]
                    self.grow_pop()
                else:
                    self.kill_pop(pop)
            except KeyError:
                pop.inventory['food'] = []
                if len(pop.inventory['food']) >= pop.food_need:
                    pop.inventory["food"] = pop.inventory["food"][
                                            :-pop.food_need]
                    self.grow_pop()
                else:
                    self.kill_pop(pop)

    def kill_pop(self, pop):
        self.village.pops = self.village.pops[:-1]
        self.village.place.grid.world.dead_pops.append(pop)
        try:
            self.village.place.changed_values['dead'] += 1
        except KeyError:
            self.village.place.changed_values['dead'] = 1

    def grow_pop(self):
        if np.random.random() * 100 <= 3:
            self.village.pops.append(Pop(self.village))
