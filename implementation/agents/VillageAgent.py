from implementation.goods.Food import Food
from structure.Agent import Agent


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
            for i in range(pop.foodneed):
                try:
                    pop.inventory["food"].pop()
                except IndexError:
                    if len(pop.inventory["food"]) == 0:
                        self.kill_pop(pop)

    def kill_pop(self, pop):
        self.village.pops.remove(pop)
        self.village.place.grid.world.dead_pops.append(pop)
        try:
            self.village.place.changed_values['dead'] += 1
        except KeyError:
            self.village.place.changed_values['dead'] = 1
