# create a function that takes in a list
# and returns a list with the reverse order

# def reverse_list(l):
#   """Returns new list with the reversed order of element."""
#   return l[::-1]

def reverse_list(l):
    """ Returns the reversed list. """
    for i in range(int(len(l)/2)):
        l[i], l[-1-i] = l[-1-i], l[i]
    return l


print(reverse_list([1, 2, 3, 4]))
print(reverse_list([3, 1, 2, 5, 4]))
