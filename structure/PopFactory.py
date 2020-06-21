from implementation.pops.FarmerPop import FarmerPop


class PopFactory:

    @classmethod
    def generate_pops(cls, settlement, food_need, job='none'):
        if job == 'farmer':
            return FarmerPop(settlement, job, food_need)
        else:
            raise ValueError('No such Job defined: ', job)
