import numpy as np

from implementation.goods.Food import Food
from structure.Agent import Agent
from structure.PopFactory import PopFactory


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
                pop.inventory["food"].append(food)

    def eat(self):
        new_pops = 0
        dying_pops = []
        for pop in self.village.pops:
            if len(pop.inventory['food']) >= pop.food_need:
                pop.inventory["food"] = pop.inventory["food"][
                                        :-pop.food_need]
                new_pops += 1
            else:
                dying_pops.append(pop)
        if dying_pops:
            self.kill_pops(dying_pops)
        self.grow_pop(new_pops)

    def kill_pop(self, pop):
        self.village.pops.remove(pop)
        self.village.place.grid.world.dead_pops.append(pop)
        if self.village.place.changed_values.get('dead') is not None:
            self.village.place.changed_values['dead'] += 1
        else:
            self.village.place.changed_values['dead'] = 1

    def kill_pops(self, pops):
        self.village.pops = [x for x in self.village.pops if x not in pops]
        self.village.place.grid.world.dead_pops.extend(pops)
        if self.village.place.changed_values.get('dead') is not None:
            self.village.place.changed_values['dead'] += len(pops)
        else:
            self.village.place.changed_values['dead'] = len(pops)
        self.village.place.changed_values['starving'] = True

    def grow_pop(self, new_pops):
        for _ in range(new_pops):
            if np.random.random() * 100 <= 3:
                PopFactory.generate_pops(self.village, food_need=2)
        if self.village.place.changed_values.get('new_pops') is not None:
            self.village.place.changed_values['new_pops'] += len(
                self.village.pops)
        else:
            self.village.place.changed_values['new_pops'] = len(
                self.village.pops)
