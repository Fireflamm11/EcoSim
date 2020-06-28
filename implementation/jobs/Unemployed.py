from structure.jobs.Job import Job


class Unemployed(Job):
    @classmethod
    def work(cls, agent, **kwargs):
        pass

    @classmethod
    def get_resources(cls, agent, **kwargs):
        pass

    @classmethod
    def on_migration(cls, pop, **kwargs):
        pass
