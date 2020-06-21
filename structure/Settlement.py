class Settlement:

    def __init__(self, place):
        self.place = place
        self.pops = []
        self.agents = []

        self.food = 0

        self.buildings = []

    def step(self):
        for agent in self.agents:
            agent.step()
