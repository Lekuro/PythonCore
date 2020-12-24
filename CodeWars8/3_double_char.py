# Given a string, you have to return a string in which
# each character (case-sensitive) is repeated once.
# double_char("String") ==> "SSttrriinngg"
# double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
# double_char("1234!_ ") ==> "11223344!!__  "

def double_char(s):
    if type(s) == str:
        return ''.join(i*2 for i in s)


print(double_char("String"))
print(double_char("Hello World"))
print(double_char("1234!_ "))
