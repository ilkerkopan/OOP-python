import turtle
from random import randint

class RaceTurtle:
    def __init__(self, color, order, start_line):
        self.race_turtle = turtle.Turtle()
        self.race_turtle.shape("turtle")
        self.race_turtle.color(color)
        self.race_turtle.penup()
        self.race_turtle.goto(start_line, order)
        self.race_turtle.pendown()
        
    def run(self):
        self.set_speed(1)
        self.race_turtle.forward(randint(5,10))
        
    def get_x_position(self):
        return self.race_turtle.xcor()
    
    def set_speed(self, speed):
        self.race_turtle.speed(speed)
