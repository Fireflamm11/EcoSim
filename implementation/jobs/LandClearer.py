from structure.jobs.Job import Job


class LandClearer(Job):
    @classmethod
    def work(cls, agent, **kwargs):
        pass

    @classmethod
    def get_resources(cls, agent, **kwargs):
        pass

    @classmethod
    def on_migration(cls, pop, **kwargs):
        pass

    @classmethod
    def on_death(cls, pop, **kwargs):
        pass
