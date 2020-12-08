n = 101

for i in range(n):
    if i % 2 == 0:
        continue
    print(i, end='_')
print()

for item in range(1, n, 2):
    print(item, end='_')
print()

print(list(range(1, n, 2)))
print([i for i in range(1, n, 2)])
