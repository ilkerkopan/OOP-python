from raceturtle import RaceTurtle
from random import randint

class FastRaceTurtle(RaceTurtle):
    def run(self):
        self.set_speed(1)
        self.race_turtle.forward(randint(1,15))