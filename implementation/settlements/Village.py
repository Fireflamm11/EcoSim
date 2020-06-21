from structure.PopFactory import PopFactory
from structure.Settlement import Settlement


class Village(Settlement):
    def __init__(self, place, start_pops):
        super().__init__(place)
        for idx in range(start_pops):
            PopFactory.generate_pops(self, 2, "farmer")
