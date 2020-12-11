# Task1. Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function).

def largest(a, b):
    """
    function returns largest of two numbers
    """
    return a if a > b else b


print(largest(3, 3))
