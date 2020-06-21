from structure.Pop import Pop


class FarmerPop(Pop):
    def __init__(self, village, job='none', food_need=1):
        super().__init__(village, job, food_need)
        self.index_owned_arable_land = []
