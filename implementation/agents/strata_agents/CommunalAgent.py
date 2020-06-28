import numpy as np

from implementation.jobs.Farmer import Farmer
from implementation.jobs.Unemployed import Unemployed
from structure.PopFactory import PopFactory
from structure.agents.StrataAgent import StrataAgent


class CommunalAgent(StrataAgent):

    # Begin of the overwritten ABC-Methods
    @classmethod
    def job_redistribution(cls, agent, **kwargs):
        if len(agent.village.job_distribution[Unemployed]) <= \
                agent.village.free_land:
            new_farmer = agent.village.free_land
            idx = np.random.randint(
                len(agent.village.job_distribution[Unemployed]),
                size=new_farmer)
            new_farmer = [agent.village.job_distribution[Unemployed][i] for i
                          in idx]
            [pop.change_job(Farmer) for pop in new_farmer]

    @classmethod
    def work(cls, agent, **kwargs):
        [job.work(agent) for job in agent.village.job_distribution]

    @classmethod
    def consume(cls, agent, **kwargs):
        agent.village.place.changed_values['starving'] = False
        new_pops = 0
        agent.village.food -= 2 * len(agent.village.pops)
        agent.starving = int(-agent.village.food / 2)
        if agent.starving > len(agent.village.pops):
            agent.starving = len(agent.village.pops)
        if agent.village.food < 0:
            health_change = -50
            agent.village.place.changed_values['starving'] = True
        else:
            health_change = 10

        for pop in agent.village.pops:
            pop.health += health_change
            new_pops += 1

        agent.village.food = 0
        cls.grow_pop(agent, new_pops)

    @classmethod
    def pop_development(cls, agent, **kwargs):
        agent.migrate_pops()
        agent.ageing()

    @classmethod
    def settlement_development(cls, agent, **kwargs):
        pass

    # End of the overwritten ABC-Methods
    # After this follows the internal logic for this strata

    @classmethod
    def grow_pop(cls, agent, new_pops):
        for _ in range(new_pops):
            if np.random.random() * 100 <= 3:
                PopFactory.generate_pops(agent.village, job='Unemployed',
                                         food_need=2)
        if agent.village.place.changed_values.get('pops') is not None:
            agent.village.place.changed_values['pops'] += len(
                agent.village.pops)
        else:
            agent.village.place.changed_values['pops'] = len(
                agent.village.pops)
