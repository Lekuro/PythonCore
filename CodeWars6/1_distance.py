# Simple: Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    """
    function count the distance between two pont (x1, y1) and (x2, y2)
    """
    return round(((x1 - x2)**2 + (y1 - y2)**2)**(1/2), 2)


print(distance(-1, -2, 1, 2))
