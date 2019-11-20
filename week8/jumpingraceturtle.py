from raceturtle import RaceTurtle
from random import randint

class JumpingRaceTurtle(RaceTurtle):
    def __init__(self, color, order, start_line):
        super().__init__(color, order, start_line)
        self.cooldown=0
        
    def run(self):
        self.set_speed(10)
        if self.cooldown == 0 :
            self.race_turtle.forward(randint(30,50))
            self.cooldown = 4
        else :
            self.cooldown -= 1