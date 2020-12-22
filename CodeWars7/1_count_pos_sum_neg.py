# Count of positives / sum of negatives

# Given an array of integers.
# Return an array, where the first element is the count of positives numbers
# and the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array.

def count_positives_sum_negatives(arr):
    count = 0
    sum = 0
    for item in arr:
        if item > 0:
            count += 1
        else:
            sum += item
    return [count, sum] if arr else []
    # return [len([x for x in arr if x > 0]), sum([y for y in arr if y < 0])] if arr else []


print(count_positives_sum_negatives(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives(
    [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
print(count_positives_sum_negatives([1]))
print(count_positives_sum_negatives([-1]))
print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(count_positives_sum_negatives([]))
