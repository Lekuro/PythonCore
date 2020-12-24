# Create a polygon class and a rectangle class
# that inherits from the polygon class and finds the square of rectangle.

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f'Enter side {str(i+1)}: '))
                      for i in range(self.n)]

    def displaySides(self):
        for i in range(self.n):
            print(f'Side {i+1} is {self.sides[i]}')


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
        #Polygon.__init__(self, 2)

    def findArea(self):
        width, height = self.sides
        return f'Area of rectangle is {width * height}'


rect = Rectangle()
rect.inputSides()
rect.displaySides()
print(rect.findArea())


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)  # super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


t = Triangle()
t.inputSides()
t.displaySides()
t.findArea()
