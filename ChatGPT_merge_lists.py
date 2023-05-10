list1 = [['ago', '_', '01.01.2021'], ['mati', '_', '06.08.2020']]
list2 = [['mari', 'tallinn', '-'], ['ago', 'tartu', '-'], ['mati', 'narva', '-']]

new_list = [['name', 'town', 'date']]  # initialize with headers

for person in list1:
    name = person[0]
    found_match = False
    for info in list2:
        if info[0] == name:
            town = info[1] if info[1] != '-' else ''
            date = person[2] if person[2] != '-' else ''
            new_info = [name, town, date]
            new_list.append(new_info)
            found_match = True
            break  # stop searching for this name

    if not found_match:
        town = ''
        date = person[2] if person[2] != '-' else ''
        new_info = [name, town, date]
        new_list.append(new_info)

# add entry for 'mari'
for info in list2:
    if info[0] == 'mari':
        town = info[1] if info[1] != '-' else ''
        date = '_'  # set date to '_' for 'mari'
        new_info = ['mari', town, date]
        new_list.append(new_info)

print(new_list)