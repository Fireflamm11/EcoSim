import numpy as np

from implementation.jobs.Farmer import Farmer
from implementation.jobs.Unemployed import Unemployed
from structure.PopFactory import PopFactory
from structure.agents.StrataAgent import StrataAgent


class CommunalAgent(StrataAgent):

    # Begin of the overwritten ABC-Methods
    @classmethod
    def job_redistribution(cls, agent, **kwargs):
        if agent.village.free_land == 0:
            return

        if len(agent.village.job_distribution[Unemployed]) <= \
                agent.village.free_land:
            new_farmer = min(agent.village.free_land,
                             len(agent.village.job_distribution[Unemployed]))
            agent.village.free_land -= new_farmer

            idx = np.random.default_rng().choice(
                len(agent.village.job_distribution[Unemployed]),
                size=new_farmer, replace=False)
            new_farmer = [agent.village.job_distribution[Unemployed][i] for i
                          in idx]
            [pop.change_job(Farmer) for pop in new_farmer]

    @classmethod
    def work(cls, agent, **kwargs):
        [job.work(agent) for job in agent.village.job_distribution]

    @classmethod
    def consume(cls, agent, **kwargs):
        if len(agent.village.pops) == 0:
            return

        agent.village.place.changed_values['starving'] = False
        new_pops = 0
        for job in agent.village.job_types:
            agent.light_starving[job] = 0
            agent.heavy_starving[job] = 0
        print(11111111111111111111111111111111111111111111111111111111111111111111)
        print(agent.village.food)
        print(len(agent.village.pops))
        print(len(agent.village.job_distribution[Farmer]))
# try to do new food system system based on jobs, Farmer will first try to feed themselves, than other jobs,
# than unemployed?
# differentiate between light and heavy starving for pops, whether they can feed once or twice
        if agent.village.food <= len(agent.village.job_distribution[Farmer]) * 2:
            print(2)
            agent.village.food -= len(agent.village.job_distribution[Farmer])
            agent.heavy_starving[Farmer] = int(-min(agent.village.food, 0))
            agent.light_starving[Farmer] = int(len(agent.village.job_distribution[Farmer]) - agent.village.food) - \
                                           (agent.heavy_starving[Farmer] * 2)
            for job in agent.village.job_types:
                if job == Farmer:
                    continue
                agent.heavy_starving[job] = len(agent.village.job_distribution[job])
                # all other pops starve completely

            """if int(-agent.village.food) <= len(agent.village.job_distribution[Farmer]):
                agent.light_starving[Farmer] = int(-agent.village.food)    # is the case when Food deficit is smaller
            else:                                                  # than pops, all pops can eat once at least
                agent.heavy_starving[Farmer] = int(-agent.village.food) - len(agent.village.job_distribution[Farmer])
                agent.light_starving[Farmer] = len(agent.village.job_distribution[Farmer]) - len(agent.heavy_starving)
                # all pops starve, some of them heavy because food deficit is greater than number of pops
                # alternative??
            for job in agent.village.job_types:
                if job == Farmer:
                    continue
                agent.heavy_starving[job] = len(agent.village.job_distribution[job])
                # all other pops starve completely"""

        # checking if enough food for all unemployed, than only those starve
        elif agent.village.food >= (len(agent.village.pops) - len(agent.village.job_distribution[Unemployed])) * 2:
            print(1)
            agent.village.food -= len(agent.village.pops)
            agent.heavy_starving[Unemployed] = int(-min(agent.village.food, 0))
            agent.light_starving[Unemployed] = int(-min(agent.village.food - len(agent.village.pops), 0)
                                                   - agent.heavy_starving[Unemployed] * 2)
        # i have literally no idea if this works, if food deficit is greater than pops, it should start giving out heavy
        # starving, lowering the amount of light starving (trying without if statement)

        else:
            print("this shouldn't jet happen, something is wrong")
        print(agent.light_starving)
        print(agent.heavy_starving)





#        agent.village.food -= 2 * len(agent.village.pops)
#        agent.starving = int(-agent.village.food / 2)
#        if agent.starving > len(agent.village.pops):
#            agent.starving = len(agent.village.pops)
#        if agent.village.food < 0:
#            health_change = -50
#            agent.village.place.changed_values['starving'] = True
#        else:
#            health_change = 10

        for pop in agent.village.pops:
            "pop.health += health_change"
            agent.village.place.weather.pop_impact(pop)
            new_pops += 1

        agent.village.food = 0
        cls.grow_pop(agent, new_pops)

    @classmethod
    def pop_development(cls, agent, **kwargs):
        agent.ageing()
        """agent.migrate_pops()"""

    @classmethod
    def settlement_development(cls, agent, **kwargs):
        pass

    # End of the overwritten ABC-Methods
    # After this follows the internal logic for this strata

    @classmethod
    def grow_pop(cls, agent, new_pops):
        for _ in range(new_pops):
            if np.random.random() * 100 <= 5:
                PopFactory.generate_pops(agent.village, job='Unemployed',
                                         food_need=2)

        if agent.village.place.changed_values.get('pops') is not None:
            agent.village.place.changed_values['pops'] += len(
                agent.village.pops)
        else:
            agent.village.place.changed_values['pops'] = len(
                agent.village.pops)
