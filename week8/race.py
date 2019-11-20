from raceturtle import RaceTurtle
from fastraceturtle import FastRaceTurtle
from jumpingraceturtle import JumpingRaceTurtle

class Race:
    def __init__(self, race_track):
        self.race_track = race_track
        self.race_track.draw_track()
        self.red_turtle = RaceTurtle("red", 50, self.race_track.starting_point)
        self.green_turtle = FastRaceTurtle("green", 0, self.race_track.starting_point)
        self.blue_turtle = JumpingRaceTurtle("blue", -50, self.race_track.starting_point)

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
