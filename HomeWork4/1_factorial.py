def factorial(x):
    factorial = 1
    if x == 0 or x == 1:
        return factorial
    if x < 0:
        return 'There is no'
    for i in range(x):
        factorial *= i + 1
    return factorial


number = int(input('Please enter a number: '))
print(f'Factorial your number is {factorial(number)}.')
