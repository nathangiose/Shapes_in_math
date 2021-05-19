from main import Shapes
class Circle(Shapes):
    def __init__(self, radius, pi):
        self.radius = (radius*radius)
        self.pi = (3.14)
    def Area(self):
        result = self.radius * self.pi
        return result

obj_watch = Circle(3, 7)
obj_cup = (5, 7)
print("The area if a cup is " + str(obj_watch.Area()))

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def Area(self):
        result = (self.base * self.height)/2
        return result

obj_pyrimad = Triangle(10, 7)
print("The area if a pyrimad is " + str(obj_pyrimad.Area()))
