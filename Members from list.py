def members_from_list():
    my_list = [1, 2, 345, 56, 4, 8, 99, 34, 68, 9, 4, 3, 854, 6, 84, 4, 6, 9, 0]
    new_list = []
    for element in my_list:
        if element < 5:
            new_list.append(element)
    print(new_list)
    ask_number = input("Please enter a number: ")
    for element in my_list:
        if element < int(ask_number):
            new_list.append(element)
    print(new_list)

members_from_list()