from mesa import Agent, Model
from mesa.datacollection import DataCollector
import random


def compute_gini(model):

    wealths = sorted([a.wealth for a in model.agents])
    n = len(wealths)
    total = sum(wealths)
    if total == 0:
        return 0

    cumulative = sum((i + 1) * w for i, w in enumerate(wealths))
    return round((2 * cumulative) / (n * total) - (n+1) / n, 3)


class WealthAgent(Agent):
    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1

    def step(self):
        if self.wealth == 0:
            return

        others = [a for a in self.model.agents if a is not self]
        other = self.random.choice(others)

        self.wealth -= 1
        other.wealth += 1


class WealthModel(Model):
    def __init__(self, n_agents):
        super().__init__()

        for _ in range(n_agents):
            WealthAgent(self)

        self.datacollector = DataCollector(
            model_reporters={
                "Gini": compute_gini,
                "Max wealth": lambda m: max(a.wealth for a in m.agents),
                "Broke": lambda m: sum(1 for a in m.agents if a.wealth == 0),
            },
            agent_reporters={
                "Wealth": "wealth"
            }
        )

    def step(self):
        self.datacollector.collect(self)
        self.agents.shuffle_do("step")


model = WealthModel(n_agents=50)
for _ in range(100):
    model.step()

model_df = model.datacollector.get_model_vars_dataframe()
agent_df = model.datacollector.get_agent_vars_dataframe()


print(model_df.tail())        # last 5 steps of model-level data
print(agent_df.tail(10))
