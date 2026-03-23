from mesa import Agent, Model
import random


class HelloAgent(Agent):
    def __init__(self, model):
        super().__init__(model)
        self.wealth = random.randint(1, 10)       # your job: random value 1–10


    def step(self):
        print(f"Agent {self.unique_id} have {self.wealth} money")                # your job: print the wealth


class HelloModel(Model):
    def __init__(self, n_agents):
        super().__init__()


        for i in range(n_agents):
            HelloAgent(self)

    def step(self):
        self.agents.shuffle_do("step")


model = HelloModel(20)

model.step()