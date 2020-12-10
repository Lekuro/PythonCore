# Task Overview:
# You have to write a function that accepts three parameters:

# cap is the amount of people the bus can hold excluding the driver.
# on is the number of people on the bus excluding the driver.
# wait is the number of people waiting to get on to the bus excluding the driver.
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

def enough(cap, on, wait):
    '''
    :param cap: total number of seats
    :param on: number of passengers on the bus
    :param wait: number of passengers waiting for the bus
    :return: number of passengers that can't enter the bus
    '''
    if cap < on:
        return 'Error: the bus cannot hold such amount of people'
    return 0 if cap - on >= wait else wait - (cap - on)


print(enough(40, 50, 3))
