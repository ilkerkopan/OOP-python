import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def calculate_distance(self):
        return math.sqrt((self.x*self.x) + (self.y*self.y))
    

point1 = Point(3,4)
point2 = Point(2,8)
print(point1.calculate_distance())
print(point2.calculate_distance())