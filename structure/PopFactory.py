from implementation.jobs.Farmer import Farmer
from implementation.jobs.Unemployed import Unemployed
from implementation.pops.FarmerPop import FarmerPop
from structure.pops.Pop import Pop


class PopFactory:

    @classmethod
    def generate_pops(cls, settlement, food_need, job='none'):
        if job == 'Farmer':
            return FarmerPop(settlement, Farmer, food_need)
        elif job == 'Unemployed':
            return Pop(settlement, Unemployed, food_need)
        else:
            raise ValueError('No such Job defined: ', job)
