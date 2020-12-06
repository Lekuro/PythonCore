# Задано чотирицифрове натуральне число.
# - Знайти добуток цифр цього числа.
# - Записати число в реверсному порядку.
# - Посортувати цифри, що входять в дане число

num = 4132
print('number =', num)

# 1
num_str = str(num)
digits = []
product = 1
for i in num_str:
    ii = int(i)
    digits.append(ii)
    product *= ii
# print(digits)
print(f"The product of digits is {product}.")
# 2
reversed_digits = digits[:]
reversed_digits.reverse()
# print(reversed_digits)
num_reversed = 0
len_digits = len(digits)
for i in range(len_digits):
    num_reversed += reversed_digits[i]*10**(len_digits-i-1)
print(f'The reversed number is {num_reversed}.')
# 3
sorted_digits = digits.copy()
sorted_digits.sort()
# print(sorted_digits)
num_sorted = 0
len_digits = len(digits)
for i in range(len_digits):
    num_sorted += sorted_digits[i]*10**(len_digits-i-1)
print(f'The sorted number is {num_sorted}.')
