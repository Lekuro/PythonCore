# Consider an array/list of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheeps):
    """
    function count True in collection sheep
    param sheeps - is a collection of sheeps
    return - amount of sheeps that is True
    """
    count = 0
    for sheep in sheeps:
        if sheep:
            count += 1
    return count
