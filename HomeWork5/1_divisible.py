# Task2. In the range from 1 to 10 determine
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.

divisible2 = []
divisible3 = []
not_div_2_3 = []
for num in range(1, 11):
    if num % 2 == 0:
        divisible2.append(num)
    if num % 3 == 0:
        divisible3.append(num)
    if num % 2 != 0 and num % 3 != 0:
        not_div_2_3.append(num)

print(f'Even numbers that are divisible by 2 {divisible2}.')
print(f'Odd numbers, which are divisible by 3 {divisible3}.')
print(f'Numbers that are not divisible by 2 and 3 {not_div_2_3}.')
