import turtle

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
