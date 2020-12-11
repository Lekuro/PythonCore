# Write a function that returns the arithmetic
# mean of any number of numbers.
def arithmetic(*args):
    """
    function returns arithmetic of all given arguments
    """
    lenght = len(args)
    if lenght == 0:
        return None
    return round(sum(args)/lenght, 3)


print(arithmetic(1, 9, 4, 6, 7, 9, 9,))
