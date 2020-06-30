from structure.jobs.Job import Job


class Farmer(Job):
    @classmethod
    def work(cls, agent, **kwargs):
        agent.food_production_modifier = agent.village.place.soil_quality * agent.village.place.weather_impact
        if agent.village.free_land > 0:
            agent.village.food += agent.food_production_modifier * len(
                agent.village.job_distribution[cls])
        else:
            agent.village.food += \
                agent.food_production_modifier * agent.village.arable_land

    @classmethod
    def get_resources(cls, agent, **kwargs):
        pass

    @classmethod
    def on_migration(cls, pop, **kwargs):
        pop.village.free_land += 1

    @classmethod
    def on_death(cls, pop, **kwargs):
        pop.village.free_land += 1
