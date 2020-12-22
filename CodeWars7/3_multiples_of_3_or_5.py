# If we list all the natural numbers below 10
# that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all
# the multiples of 3 or 5 below the number passed in.

# Note: If the number is a multiple of both 3 and 5,
# only count it once. Also, if a number is negative,
# return 0(for languages that do have them)

def solution(number):
    # multiples_of_3_or_5 = []
    # for i in range(3, number):
    #     if i % 3 == 0 and i % 5 == 0:
    #         multiples_of_3_or_5.append(i)
    #     elif i % 3 == 0:
    #         multiples_of_3_or_5.append(i)
    #     elif i % 5 == 0:
    #         multiples_of_3_or_5.append(i)
    # # print(multiples_of_3_or_5)
    # return sum(multiples_of_3_or_5) if number > 0 else 0
    return sum({i for i in range(3, number) if i % 3 == 0 or i % 5 == 0})


print(solution(10))
print(solution(16))
print(solution(-1))
