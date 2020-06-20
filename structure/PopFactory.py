from structure.Pop import Pop


class PopFactory:

    @classmethod
    def generate_pops(cls, settlement, food_need, job='none'):
        return Pop(settlement, job, food_need)
