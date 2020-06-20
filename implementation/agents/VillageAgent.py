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
        new_pops = 0
        for pop in self.village.pops:
            if len(pop.inventory['food']) >= pop.food_need:
                pop.inventory["food"] = pop.inventory["food"][
                                        :-pop.food_need]
                new_pops += 1
            else:
                self.kill_pop(pop)

    def kill_pop(self, pop):
        self.village.pops.remove(pop)
        self.village.place.grid.world.dead_pops.append(pop)
        try:
            self.village.place.changed_values['dead'] += 1
        except KeyError:
            self.village.place.changed_values['dead'] = 1

    def grow_pop(self, new_pops):
        for _ in new_pops:
            if np.random.random() * 100 <= 3:
                self.village.pops.append(Pop(self.village))
