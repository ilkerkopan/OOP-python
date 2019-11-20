import random

class Dice:
    def __init__(self, surface_count):
        self.surface_count = surface_count
        
    def roll(self):
        return random.randint(1,self.surface_count)
    

