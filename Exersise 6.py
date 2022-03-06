def number_in_list(list, multiple):
    new_list = []
    for num in list:
        if num % multiple == 0:
            new_list.append(num)
    return new_list
