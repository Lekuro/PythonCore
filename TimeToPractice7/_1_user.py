import _1_calculator as calc
# Написати скрипт- calculator.py, в якому створюєте функції додавання, віднімання, множення, ділення,
# а в іншому модулі запитуєте користувача, яку дію він хоче виконати і з якими числами.

try:
    num1 = float(input('Please enter a number '))
    num2 = float(input('Please enter a number '))
    act = input('Please enter what you want to do: +, -, * or / ')
    if act not in ('+', '-', '*', '/'):
        print('You enter incorrect data i take "+". Sorry.')
        act = '+'
except:
    print('You enter incorrect numbers i take num1 = 5, num2 = 3. Sorry.')
    num1 = 5
    num2 = 3

if act == '+':
    print('num1 + num2 = ', calc.add(num1, num2))
elif act == '-':
    print('num1 - num2 = ', calc.sub(num1, num2))
elif act == '*':
    print('num1 * num2 = ', calc.mul(num1, num2))
elif act == '/':
    print('num1 / num2 = ', calc.div(num1, num2))
