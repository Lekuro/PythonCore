# Write a program that analyzes
# the entered number and,
# depending on the number,
# gives the day of the week
# that corresponds to this number
# (1 is Monday, 2 is Tuesday, etc.).
# Take into account cases of
# entering numbers from 8 and more,
# as well as cases of
# entering non-numerical data.

class CustomError(Exception):
    pass


days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
        4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
try:
    day = int(input("Enter an integer number: "))
    if day <= 0:
        raise CustomError("A number of day can't be negative or zero!")
    elif day > 7:
        day %= 7
    print(f'The day {day} is {days[day]}.')
except ValueError as e:
    print(e)
except CustomError as e:
    print(f'You enter incorrect data. \nException: {e}')
