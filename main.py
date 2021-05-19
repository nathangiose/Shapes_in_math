class Shapes:
    def __init__(self, name, side):
        self.name = name
        self.side = side
    def Area(self):
        print("I am a: " + self.name + "\n" +
              "I have " + self.side + "side")

obj_shape=Shapes("shape", "so many ")
obj_shape.Area()

class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length = len1
        self.width = wid1
    def Area(self):
        result = self.length * self.width
        return result

obj_book = Rectangle(10, 7)
obj_screen = (5, 7)
print("The area if a book is " + str(obj_book.Area()))
