with open("C:/Users/Arvuti3/Documents/test_file.txt", "r") as names:
    all_names = names.read()
    list_names = list(all_names.split("\n"))
    my_dict = {i: list_names.count(i) for i in list_names}
    print(my_dict)
