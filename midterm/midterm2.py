import math

class Circle():
    def __init__(self, radius):
        self.radius= radius
    
    def getArea(self):
        return self.radius * self.radius * math.pi
    
    def getRadius(self):
        return self.radius