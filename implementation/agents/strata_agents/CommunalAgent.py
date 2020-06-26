from random import shuffle

import numpy as np

from structure.PopFactory import PopFactory
from structure.agents.StrataAgent import StrataAgent


class CommunalAgent(StrataAgent):

    # Begin of the overwritten ABC-Methods
    @classmethod
    def work(cls, agent, **kwargs):
        for _ in range(agent.village.place.soil_quality):
            # TODO why iterate over soil_quality
            if len(agent.village.pops) <= agent.village.arable_land:
                agent.village.food += len(agent.village.pops)
            else:
                agent.village.food += agent.village.arable_land

    @classmethod
    def consume(cls, agent, **kwargs):
        agent.village.place.changed_values['starving'] = False
        new_pops = 0
        agent.village.food += agent.village.place.soil_quality * len(
            agent.village.pops)
        # TODO why negative? And why class variable(its get overwritten)
        pops = agent.village.pops.copy()
        shuffle(pops)
        for pop in pops:
            if agent.village.food > 0:
                pop.health += 10
                new_pops += 1
                agent.village.food -= pop.food_need
            else:
                pop.health -= 50
                new_pops += 1
                agent.starving.append(pop)
                agent.village.place.changed_values['starving'] = True
        cls.grow_pop(agent, new_pops)

    @classmethod
    def pop_development(cls, agent, **kwargs):
        agent.ageing()
        agent.migrate_pops()

    @classmethod
    def settlement_development(cls, agent, **kwargs):
        pass

    # End of the overwritten ABC-Methods
    # After this follows the internal logic for this strata

    @classmethod
    def grow_pop(cls, agent, new_pops):
        for _ in range(new_pops):
            if np.random.random() * 100 <= 3:
                PopFactory.generate_pops(agent.village, job='farmer',
                                         food_need=2)
        if agent.village.place.changed_values.get('pops') is not None:
            agent.village.place.changed_values['pops'] += len(
                agent.village.pops)
        else:
            agent.village.place.changed_values['pops'] = len(
                agent.village.pops)
