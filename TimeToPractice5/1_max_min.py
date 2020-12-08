amount = int(input('Please enter number of numbers '))

numbers = [input('enter next number ') for i in range(amount)]
print('Maximum is ', max(numbers))
print('Minimum is ', min(numbers))
