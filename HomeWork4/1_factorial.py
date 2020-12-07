def factorial(x):
    factorial = 1
    for i in range(x):
        factorial *= i + 1
    return factorial


print(factorial(5))
