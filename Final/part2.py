from func_part2 import *
# get string from file
lines = []
with open('data.txt', 'r') as file:
    for line in file:
        if line[-1:] == '\n':
            lines.append(line[:-1])
        else:
            lines.append(line)

# part by ' bags contain ' create dict with key like name of bags, value is everything else
# and list of all bags inside shiny gold bag
d_bags = {}  # dict with unigue bags
magic = 'shiny gold'
for line in lines:
    parted_bag = line.split(' bags contain ')
    if parted_bag[0] == magic:
        # it is list of bags inside magic bag
        l_bags = parted_bag[1].split(', ')
        l_bags[-1] = l_bags[-1][:-1]
    d_bags[parted_bag[0]] = parted_bag[1]

print_bags(l_bags)
counter = 0
while check_bag(l_bags):
    print('check_bag()', check_bag(l_bags))
    # this loop takes a bag, parts it and gets the key,
    # look for key in d_bags contained bags
    # and insert finded bags for place of this bag
    for index in range(len(l_bags)):
        if l_bags[index] == 'no other bags':
            continue
        parted = l_bags[index].split()
        count = int(parted[0])
        counter += count
        key = ' '.join(parted[1:-1])
        if key != 'shiny gold':
            l_bags[index] = d_bags[key] * count
            if l_bags[index][-1] == '.':
                l_bags[index] = l_bags[index][:-1]
            if '.' in l_bags[index]:
                l_bags[index] = l_bags[index].split('.')
                l_bags[index] = ', '.join(l_bags[index])
    print('finish deeper')
    part_bag(l_bags)
    print('lenght of magic:', len(l_bags))
    print('counter', counter)

# print_bags()
