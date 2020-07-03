from implementation.jobs.Unemployed import Unemployed


class Pop:
    def __init__(self, village, job=Unemployed, food_need=1):
        self.inventory = {}
        self.village = village
        self.village.pops.append(self)
        self.age = 18
        self.job = job
        self.village.job_distribution[job].append(self)
        self.food_need = food_need
        self.health = 100

        self.inventory['food'] = []

    def change_job(self, new_job):
        self.village.job_distribution[self.job].remove(self)
        self.job = new_job
        self.village.job_distribution[self.job].append(self)

    def on_migration(self, new_village):
        self.job.on_migration(self)
        self.village.pops.remove(self)
        self.village.job_distribution[self.job].remove(self)
        self.job = Unemployed
        self.village = new_village
        self.village.pops.append(self)
        self.village.job_distribution[self.job].append(self)

    def on_death(self):
        self.village.job_distribution[self.job].remove(self)
        self.village.pops.remove(self)
        self.job.on_death(self)
