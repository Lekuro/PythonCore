# Task3. Write a function that calculates
# the number of characters included in a given string

entered = input('Please enter something ')
if entered:
    symbol_amount = {}
    for i in entered:
        symbol_amount[i] = entered.count(i)
    print(symbol_amount)
else:
    print('Incorrect data!!!')
