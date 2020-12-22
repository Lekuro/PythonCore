from math import (pow as power,
                  pi as PI)

if __name__ != '__main__':
    def rectangle_square(width, height):
        '''calculates the square of a rectangle'''
        return width * height

    def triangle_square(base, height):
        '''calculates the square of a triangle'''
        return base * height / 2

    def circle_square(radius):
        '''calculates the square of a circle'''
        return round(PI * power(radius, 2), 3)
