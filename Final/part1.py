from func_part1 import *
# get string from file 169
lines = []
with open('data.txt', 'r') as file:
    for line in file:
        if line[-1:] == '\n':
            lines.append(line[:-1])
        else:
            lines.append(line)
# print(lines)

# parts by ' bags contain ' create dict with key like name of bags, value is everything else
# and list of all bags first part name of bags second is everything else
d_bags = {}
l_bags = []
magic = 'shiny gold'
for line in lines:
    parted_bag = line.split(' bags contain ')
    if parted_bag[1] == 'no other bags.':
        parted_bag[1] = ''
    l_bags.append(parted_bag)
    d_bags[parted_bag[0]] = parted_bag[1]


print_bags(l_bags)


while check_bags(l_bags):
    clean_bags(l_bags, d_bags)
    print('I still work')

# amount of 'shiny gold'
count = 0
for line in l_bags:
    if '' == line[1] or line[0] == 'shiny gold':
        continue
    if 'shiny gold' in line[1]:
        count += 1
print(count)
print_bags(l_bags)
print(count)
