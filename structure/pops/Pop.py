class Pop:
    def __init__(self, village, job='Unemployed', food_need=1):
        self.inventory = {}
        self.village = village
        self.village.pops.append(self)
        self.age = 18
        self.job = job
        self.village.job_distribution[job].append(self)
        self.food_need = food_need
        self.health = 100

        self.inventory['food'] = []

        self.village.job_distribution["Unemployed"].append(self)

    def change_job(self, new_job):
        self.village.job_distribution[self.job].remove(self)
        self.job = new_job
        self.village.job_distribution[self.job].append(self)

    def on_migration(self, new_village):
        # TODO Better management to free resources when migrating
        if self.job == 'Farmer':
            self.village.free_land += 1
        self.village.job_distribution[self.job].remove(self)
        self.job = 'Unemployed'
        self.village = new_village
        self.village.job_distribution[self.job].append(self)
