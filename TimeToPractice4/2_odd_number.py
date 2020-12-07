n = 100

for i in range(n):
    if i % 2 == 0:
        continue
    print(i, end='_')
print()

i = 0
while i < n:
    if i % 2 == 1:
        print(i, end='_')
    i += 1
