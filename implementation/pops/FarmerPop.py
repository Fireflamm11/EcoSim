from structure.pops.Pop import Pop


class FarmerPop(Pop):
    def __init__(self, village, job='Farmer', food_need=2):
        super().__init__(village, job, food_need)
        self.index_owned_arable_land = []
