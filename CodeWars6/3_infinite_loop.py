# Unfinished Loop - Bug Fixing #1
# Oh no, Timmy's created an infinite loop!
# Help Timmy find and fix the bug in his unfinished for loop!

def create_array(n):
    """
    function return list from 1 to n with step 1
    """
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1
    return res


print(create_array(10))
