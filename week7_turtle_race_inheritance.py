import turtle
from random import randint

class RaceTrack:
    def __init__(self, start, end):
        self.starting_point = start
        self.finish_point = end
    
    def draw_track(self):
        drawer = turtle.Turtle()
        drawer.penup()
        drawer.right(90)
        start_x = self.starting_point
        track_length = -self.starting_point + self.finish_point
        for i in range(0,track_length+1,50):
            drawer.goto(start_x+i,100)
            drawer.pendown()
            drawer.forward(200)
            drawer.penup()
            drawer.forward(10)
            drawer.write(i)

class LongRaceTrack(RaceTrack):
    def __init__(self):
        super().__init__(-200,300)

class ShortRaceTrack(RaceTrack):
    def __init__(self):
        super().__init__(-100,100)
        
class RaceTurtle:
    def __init__(self, color, order, start_line):
        self.race_turtle = turtle.Turtle()
        self.race_turtle.shape("turtle")
        self.race_turtle.color(color)
        self.race_turtle.penup()
        self.race_turtle.goto(start_line, order)
        self.race_turtle.pendown()
        
    def run(self):
        self.race_turtle.forward(randint(1,10))
        
    def get_x_position(self):
        return self.race_turtle.xcor()

class Race:
    def __init__(self, race_track):
        self.race_track = race_track
        self.race_track.draw_track()
        self.red_turtle = RaceTurtle("red", 50, self.race_track.starting_point)
        self.green_turtle = RaceTurtle("green", 0, self.race_track.starting_point)
        self.blue_turtle = RaceTurtle("blue", -50, self.race_track.starting_point)

    def start_race(self):
        self.not_finished = True
        while self.not_finished:
            self.red_turtle.run()
            self.green_turtle.run()
            self.blue_turtle.run()
            if self.red_turtle.get_x_position() >= self.race_track.finish_point:
                self.not_finished = False
                print("Red turtle wins")
            elif self.green_turtle.get_x_position() >= self.race_track.finish_point:
                self.not_finished = False
                print("Green turtle wins")
            elif self.blue_turtle.get_x_position() >= self.race_track.finish_point:
                self.not_finished = False
                print("Blue turtle wins")

long_race_track = LongRaceTrack()
short_race_track = ShortRaceTrack()
race = Race(short_race_track)
race.start_race()
            
