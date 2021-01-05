def print_bags(l_bags):
    """
    print bags like dict and shiny gold bags 
    """
    print('------------------------------------')
    print('Magic bag', l_bags)
    # for key in d_bags:
    #     print('key =', key, 'val =', d_bags[key])


def part_bag(l_bags):
    """
    function go through l_bags and split(', ') every element
    """
    index = 0
    while index < len(l_bags):
        if ', ' in l_bags[index]:
            bags = l_bags[index].split(', ')
            l_bags[index:index + 1] = bags
        index += 1
    print('----part_bag------')


def check_bag(l_bags):
    '''
    function go through l_bags and look for bags
    return: True if find something else than 'no other bags'
    return: False if there is no bags
    '''
    for bag in l_bags:
        if bag != 'no other bags':
            return True
    return False
