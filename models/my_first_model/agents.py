import mesa

import matplotlib.pyplot as plt

print(mesa.__version__)


class MoneyAgent(mesa.Agent):

    def __init__(self, model):

        super().__init__(model)

        self.wealth = 1

    def step(self):
        if self.wealth == 0:
            return
        other_agent = self.random.choice(self.model.agents)
        other_agent.wealth += 1
        self.wealth -= 1


class MoneyModel(mesa.Model):

    def __init__(self, N, width, height, seed=None, torus=True):
        super().__init__(seed=seed)

        self.grid = mesa.space.MultiGrid(width, height, torus=True)

        self.num_agents = N

        for i in range(self.num_agents):
            a = MoneyAgent(self)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.agents.shuffle_do("step")
    
    def move(self):


Model = MoneyModel(10, 5, 4, seed=99)

for _ in range(10):
    Model.step()


agent_wealth = [a.wealth for a in Model.agents]
plt.hist(agent_wealth)


all_wealth = []

for j in range(100):
    model = MoneyModel(10, 5, 4, seed=99)
    for i in range(10):
        model.step()

    for agent in model.agents:
        all_wealth.append(agent.wealth)

# print(all_wealth)
plt.hist(all_wealth, bins=range(max(all_wealth) + 1))
plt.xlabel("Wealth")
plt.ylabel("Number of Agents")
plt.show()
