# Задано чотирицифрове натуральне число.
# - Знайти добуток цифр цього числа.
# - Записати число в реверсному порядку.
# - Посортувати цифри, що входять в дане число

num = 4135261
print('number =', num)

# 1
num_str = str(num)
product = 1
for i in num_str:
    product *= int(i)
print(f"The product of digits is {product}.")
# 2
print(f'The reversed number is {int(num_str[::-1])}.')
# 3
str_digits = list(num_str)
str_digits.sort()
# print(str_digits)
str_num_sorted = ''.join(str_digits)
print(f'The sorted number is {int(str_num_sorted)}.')
