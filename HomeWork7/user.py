from squares import *
# (rectangle_square,
#  triangle_square,
#  circle_square)

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
        square = rectangle_square(width, height)
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
