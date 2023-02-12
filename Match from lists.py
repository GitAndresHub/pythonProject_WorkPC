import random


def match_from_lists():
    list_1 = random.sample(range(100), 25)
    list_2 = random.sample(range(100), 40)
    match_list = []
    #  match_list = [element in list_1 for element in list_2 if element == element]
    for element in list_1:
        if element == element in list_2 not in match_list:
            match_list.append(element)

    print(match_list)


match_from_lists()
