import re
# Write a Python program to check 
# the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

password = input('''Please enter you password for rules:
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters. Try: ''')
while True:
    if (re.search(r'[a-z]+', password) and
        re.search(r'[A-Z]+', password) and
        re.search(r'[0-9]+', password) and
        re.search(r'[$#@]+', password) and
        len(password) >= 6 and
        len(password) <= 16 and
            not re.search(r'[^a-zA-Z0-9$#@]', password)):
        print('valid')
        break
    else:
        password = input('No valid password try one more time: ')
