import numpy as np

from structure.AgentStrata import AgentStrata
from structure.PopFactory import PopFactory


class Communal(AgentStrata):

    @classmethod
    def production(cls, agent, **kwargs):
        for _ in range(agent.village.place.soil_quality):
            if len(agent.village.pops) <= agent.village.arable_land:
                agent.village.food += len(agent.village.pops)
            else:
                agent.village.food += agent.village.arable_land

    @classmethod
    def supply(cls, agent, **kwargs):
        new_pops = 0
        agent.village.food -= 2 * len(agent.village.pops)
        starving = int(-agent.village.food)
        if starving > len(agent.village.pops):
            starving = len(agent.village.pops)
        if agent.village.food < 0:
            for pop in agent.village.pops:
                pop.health -= 50
                new_pops += 1
        else:
            for pop in agent.village.pops:
                pop.health += 10
                new_pops += 1
                agent.village.food = 0
        cls.migrate_pop(agent, starving)
        agent.village.food = 0
        cls.grow_pop(agent, new_pops)

    @classmethod
    def pop_development(cls, agent, **kwargs):
        for pop in agent.village.pops:
            pop.age += 1
            if pop.age >= 30:
                pop.health -= 10
            if pop.age >= 40:
                pop.health -= 10
            if pop.health <= 0:
                cls.kill_pop(agent, pop)

    @classmethod
    def kill_pop(cls, agent, pop):
        agent.village.pops.remove(pop)
        if agent.village.place.changed_values.get('dead') is not None:
            agent.village.place.changed_values['dead'] += 1
        else:
            agent.village.place.changed_values['dead'] = 1

    @classmethod
    def kill_pops(cls, agent, pops):
        agent.village.pops = [x for x in agent.village.pops if x not in pops]
        agent.village.place.grid.world.dead_pops.extend(pops)
        if agent.village.place.changed_values.get('dead') is not None:
            agent.village.place.changed_values['dead'] += len(pops)
        else:
            agent.village.place.changed_values['dead'] = len(pops)
        agent.village.place.changed_values['starving'] = True

    @classmethod
    def grow_pop(cls, agent, new_pops):
        for _ in range(new_pops):
            if np.random.random() * 100 <= 33:
                PopFactory.generate_pops(agent.village, job='farmer',
                                         food_need=2)
        if agent.village.place.changed_values.get('new_pops') is not None:
            agent.village.place.changed_values['new_pops'] += len(
                agent.village.pops)
        else:
            agent.village.place.changed_values['new_pops'] = len(
                agent.village.pops)

    @classmethod
    def migrate_pop(cls, agent, starving):
        moving = []
        for pop in range(starving):
            moving.append(agent.village.pops[pop])
        agent.village.pops = [x for x in agent.village.pops if x not in moving]
        for direction in agent.village.place.directions:
            neighbor = agent.village.place.neighbors[direction]

            for settlement in neighbor.settlements:
                if settlement.arable_land - len(settlement.pops) > 0:
                    settlement.pops.extend(moving)
