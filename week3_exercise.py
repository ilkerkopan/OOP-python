import math

class Circle():
    def __init__(self, radius):
        self.radius= radius
        
    
    def getArea(self):
        return self.radius * self.radius * math.pi
    
class Rectangle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getArea(self):
        return self.x * self.y

my_circle = Circle(5)
print(my_circle.getArea())

small_rectangle = Rectangle(2,5)
big_rectangle = Rectangle(10,30)
print(f'small rectangle has an area of:{small_rectangle.getArea()}')
print(f'big rectangle has an area of:{big_rectangle.getArea()}')