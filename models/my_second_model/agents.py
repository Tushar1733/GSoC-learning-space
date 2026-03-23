import numpy as np
import pandas as pd
import seaborn as sns

import mesa

class MoneyAgent(mesa.Agent):
    def __init__(self, model):

        super().__init__(model)

        self.wealth = 1

    def say_hi(self):
        print(f"Hii, i am mesa Agent and my unique id is {self.unique_id}")


class MoneyModel(mesa.Model):
    def __init__(self, n=10, rng=None):

        super().__init__(rng=rng)

        self.num_agents = n

        MoneyAgent.create_agents(model=self, n=n)

    def step(self):

        self.agents.shuffle_do("say_hi")


pancho = MoneyModel(10)
pancho.step()
