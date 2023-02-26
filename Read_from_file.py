with open("C:/Users/Arvuti3/Documents/test_file.txt", "r") as names:
    all_names = names.read()
    list_names = list(all_names.split("\n"))
    my_dict = {i: list_names.count(i) for i in list_names}
    print(my_dict)

counter_dict = {}
with open("C:/Users/Arvuti3/Documents/test_file.txt", "r") as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)
