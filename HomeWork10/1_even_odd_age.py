# Write a program that prompts
# the user to enter their age,
# and then displays a message
# stating whether the age is even or odd.
# The program must provide the ability
# to enter a negative number,
# and in this case generate an exception.
# The master code should call a function
# that processes the information entered.
class CustomError(Exception):
    pass


# print(ValueError.mro())
# print(TypeError.mro())
try:
    age = int(input("Enter your age: "))
    if age <= 0:
        raise CustomError("An age can't be negative or zero!")
    even_or_odd = 'even' if age % 2 == 0 else 'odd'
    print(f'The age {age} is {even_or_odd}.')
except ValueError as e:
    print(e)
except CustomError as e:
    print(f'You enter incorrect data. \nException: {e}')
