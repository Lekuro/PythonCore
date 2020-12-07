def fibonachi(n):
    first = 0
    second = 1
    if n == 0:
        return first
    if n == 1:
        return second
    if n < 0:
        while n < 0:
            n += 1
            second, first = first, second - first
        return first
    while n > 1:
        n -= 1
    # for i in range(1, n):
        first, second = second, first + second
    return second


for i in range(-14, 15):
    print(f'Fibonachi {i} =', fibonachi(i))
