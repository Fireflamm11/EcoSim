class Pop:
    def __init__(self, village, job='none', food_need=1):
        self.inventory = {}
        self.village = village
        self.village.pops.append(self)
        self.age = 18
        self.job = job
        self.food_need = food_need
        self.health = 100

        self.inventory['food'] = []