def print_bags(l_bags):
    """
    print bags in list and bags like dict
    """
    print('------------------------------------')
    for bag in l_bags:
        print(bag)
    # for key in d_bags:
    #     print('key =', key, 'val =', d_bags[key])


def clean_bags(l_bags, d_bags):
    """
    line[1] partes by ', ' and replace other bag on 'shiny gold'
    """
    for line in l_bags:
        if '' == line[1] or line[0] == 'shiny gold':
            continue
        parted_kinds = line[1].split(', ')
        for index in range(len(parted_kinds)):
            parted = parted_kinds[index].split()
            parted = parted[1:-1]
            key = ' '.join(parted)
            if key != 'shiny gold':
                parted_kinds[index] = d_bags[key]
        filtered = list(filter(lambda item: item != '', parted_kinds))
        if filtered:
            line[1] = ', '.join(filtered)
        else:
            line[1] = ''


def check_bags(l_bags):
    """
    line[1] partes by ', ' and looks for other bag than 'shiny gold' 
    return: True if there is other bag than shiny gold
    return: False if there are only shiny gold
    """
    for line in l_bags:
        if '' == line[1] or line[0] == 'shiny gold':
            continue
        parted_kinds = line[1].split(', ')
        for index in range(len(parted_kinds)):
            parted = parted_kinds[index].split()
            parted = parted[1:-1]
            key = ' '.join(parted)
            if key != 'shiny gold':
                return True
    return False
