import numpy as np

from structure.Place import Place
from implementation.goods.Food import Food
from structure.Agent import Agent
from structure.PopFactory import PopFactory


class VillageAgent(Agent, Place):
    def __init__(self, village, plc):
        super().__init__()
        self.village = village
        self.place = plc

    def step(self):
        self.farm()
        self.eat()
        self.ageing()

    def farm(self):
        if self.village.strata == "communal":
            for settlement in self.village.place.settlements:
                for _ in range(self.village.place.soil_quality):
                    if len(self.village.pops) <= self.village.arable_land:
                        settlement.food += len(self.village.pops)
                    else:
                        settlement.food += self.village.arable_land

        else:
            for pop in self.village.pops:
                for i in range(self.village.place.soil_quality):
                    food = Food()
                    pop.inventory["food"].append(food)

    def eat(self):
        if self.village.strata == "communal":
            new_pops = 0
            for settlement in self.village.place.settlements:
                settlement.food -= 2 * len(self.village.pops)
                if settlement.food < 0:
                    for pop in self.village.pops:
                        pop.health -= 50
                        new_pops += 1
                else:
                    for pop in self.village.pops:
                        pop.health += 10
                        new_pops += 1
                settlement.food = 0
            self.grow_pop(new_pops)

        else:
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

    def ageing(self):
        for pop in self.village.pops:
            pop.age += 1
            if pop.age >= 30:
                pop.health -= 10
            if pop.age >= 40:
                pop.health -= 10
            if pop.health <= 0:
                self.kill_pop(pop)

    def grow_pop(self, new_pops):
        for _ in range(new_pops):
            if np.random.random() * 100 <= 30:
                PopFactory.generate_pops(self.village, food_need=2)
        if self.village.place.changed_values.get('new_pops') is not None:
            self.village.place.changed_values['new_pops'] += len(
                self.village.pops)
        else:
            self.village.place.changed_values['new_pops'] = len(
                self.village.pops)
