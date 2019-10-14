import turtle
from random import randint

class RaceArea:
    def draw_area(self):
        drawer = turtle.Turtle()
        drawer.penup()
        drawer.right(90)
        start_x=-100
        for i in range(0,250,50):
            drawer.goto(start_x+i,100)
            drawer.pendown()
            drawer.forward(200)
            drawer.penup()
            drawer.forward(10)
            drawer.write(i)

class RaceTurtle:
    def __init__(self, color, location):
        self.race_turtle = turtle.Turtle()
        self.race_turtle.shape("turtle")
        self.race_turtle.color(color)
        self.race_turtle.penup()
        self.race_turtle.goto(-100, location)
        self.race_turtle.pendown()
        
    def run(self):
        self.race_turtle.forward(randint(1,10))
        
    def get_x_position(self):
        return self.race_turtle.xcor()

race_area = RaceArea()
race_area.draw_area()
red_turtle = RaceTurtle("red", 50)
green_turtle = RaceTurtle("green", 0)
blue_turtle = RaceTurtle("blue", -50)
for i in range(40):
    red_turtle.run()
    green_turtle.run()
    blue_turtle.run()
print(red_turtle.get_x_position())
            