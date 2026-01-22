from my_abstract_class import Shape

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

sq1 = Square()
print(sq1.area(10))

rq1 = Rectangle()
print(rq1.area(10,10))

cr1 = Circle()
print(cr1.area(10))