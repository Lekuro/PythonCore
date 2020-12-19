# Task2. Write a program that calculates
# the square of ​​a rectangle, triangle and circle
# (write three functions to calculate the square,
# and call them in the main program depending on the user's choice).
from math import pi as PI


def rectangle_spuare(width, height):
    '''calculates the square of a rectangle'''
    return width * height


def triangle_square(base, height):
    '''calculates the square of a triangle'''
    return base * height / 2


def circle_square(radius):
    '''calculates the square of a circle'''
    return round(PI * radius ** 2, 3)


figures = {1: 'rectangle', 2: 'triangle', 3: 'circle'}
choose_figure = 0
while not (0 < choose_figure and choose_figure < 4):
    try:
        choose_figure = int(input('''Please enter number of geometric figure:
rectangle 1, triangle 2, circle 3
i wait '''))
    except:
        print('Please enter correct data!')

square = 'you enter bad data'
if choose_figure == 1:
    try:
        width = float(input("Please enter rectangle's width "))
        height = float(input("Please enter rectangle's height "))
        square = rectangle_spuare(width, height)
    except:
        pass
elif choose_figure == 2:
    try:
        base = float(input("Please enter triangle's base "))
        height = float(input("Please enter triangle's height "))
        square = triangle_square(base, height)
    except:
        pass
elif choose_figure == 3:
    try:
        radius = float(input("Please enter circle's radius "))
        square = circle_square(radius)
    except:
        pass

print(f'Square of {figures[choose_figure]} is ', square)
