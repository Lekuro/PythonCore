some_list = [i*i for i in range(10)]
print(some_list)

len_some_list = len(some_list)
for i in range(len_some_list):
    some_list[i] = float(some_list[i])
print(some_list)

i = 0
while i < len_some_list:
    some_list[i] = complex(some_list[i])
    i += 1
print(some_list)
