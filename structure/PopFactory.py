from structure.Pop import Pop


class PopFactory:

    @classmethod
    def generate_pops(cls, settlement, job, foodneed):
        pop = Pop(job, foodneed)
        settlement.pops.append(pop)
