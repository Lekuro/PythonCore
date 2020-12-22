import random
# Напишіть скрипт-гру, яка генерує випадковим чином число
# з діапазону чисел від 1 до 100 і пропонує користувачу вгадати це число.

# Програма зчитує числа, які вводить користувач і видає користувачу підказки
# про те чи загадане число більше чи менше за введене користувачем.
# Гра має тривати до моменту поки користувач не введе число, яке загадане програмою,
# тоді друкує повідомлення привітання.
# (для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())

secret_number = random.randint(1, 100)
print(secret_number)
guess_number = int(input('Please guess the number between 1 and 100: '))
while True:
    if guess_number == secret_number:
        print('You guessed the number!!!')
        break
    elif guess_number > secret_number:
        guess_number = int(input('Choose a smaller number: '))
    else:
        guess_number = int(input('Choose a large number: '))
