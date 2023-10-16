import numpy as np
import json
class model:
    
    def __init__(self,states_count=19,learning_rate=0.01):
        self.wieghts = np.random.rand(states_count + 1)
        self.states = []
        self.actions = []
        self.rewards = []
        self.learning_rate = learning_rate
        
    def predict(self,state):
        result = self.wieghts[0]
        for i in range(len(state)):
            result += self.wieghts[i + 1] * state[i]
        return result
    def update(self):
        pass
    def save(self):
        data = {
            'learning_rate':self.learning_rate,
            'wieghts':self.wieghts
            }
        with open("data.json", "w") as json_file:
             json.dump(data, json_file)
    def load(self):
        with open("data.json", "r") as json_file:
             data = json.load(json_file)
        self.learning_rate = data['learning_rate']
        self.wieghts = data['wieghts']
    