# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is different, send an error message.
# (need to use loop while)

login = 'First'
while True:
    if login == input('Please enter the login '):
        print(f'Welcome {login}! Is fun together!')
        break
    else:
        print('Sorry! Your login is wrong. Try one more time.')
