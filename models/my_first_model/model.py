from mesa import Agent, Model

class HelloAgent(Agent):
    def __init__(self, model):
        super().__init__(model)
        self.message = "hello"


    def step(self):
        print(f"Agent {self.unique_id} says {self.message}")


class HelloModel(Model):
    def __init__(self, n_agents):
        super().__init__()

        for i in range(n_agents):
            HelloAgent(self)

    def step(self):
        self.agents.shuffle_do("step")


model = HelloModel(10)

for tick in range(3):
    print(f"\n------step {tick}-------")
    model.step()