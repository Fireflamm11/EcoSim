from implementation.jobs.Farmer import Farmer
from implementation.jobs.LandClearer import LandClearer
from implementation.jobs.Unemployed import Unemployed
from structure.PopFactory import PopFactory
from structure.settlements.Settlement import Settlement


class Village(Settlement):
    def __init__(self, place, start_pops, strata='Communal'):
        super().__init__(place)
        self.strata = strata
        self.arable_land = self.place.arable_land / self.place.village_counter

        self.job_types = [Farmer, LandClearer, Unemployed]
        self.job_distribution = dict.fromkeys(self.job_types)
        for job in self.job_distribution:
            self.job_distribution[job] = []

        for idx in range(start_pops):
            PopFactory.generate_pops(self, 2, 'Unemployed')

        if self.arable_land < len(self.job_distribution[Farmer]):
            self.free_land = 0
        else:
            self.free_land = int(self.arable_land - len(
                self.job_distribution[Farmer]))

        # TODO Double init for lists?
        # for job_type in self.job_types:
        #     self.job_distribution[job_type] = []
