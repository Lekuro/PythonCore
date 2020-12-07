some_list = [i*i for i in range(10)]
even_list = [i for i in range(0, 10, 2)]
print(some_list, even_list)


def is_odd(list_):
    for value in list_:
        if value % 2 == 1:
            return True
    return False


print(is_odd(some_list))
print(is_odd(even_list))
