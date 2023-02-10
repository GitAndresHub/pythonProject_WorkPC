import random
def list_overlap():
    """Generate two random lists and find overlapping elements."""
    # for element in x if in y print element
    # create a function for making two random lists
    a = [] # creates an empty list a
    for i in range(0, 15): # goes through 0-14 iterations for i
        n = random.randint(1, 30) # generates a random integer n between 1 and 29
        a.append(n) # adds the random number to lis a 15 times (from range of i = 0-15)
    print(str(a))
    b = []
    for i in range(0, 10):
        n = random.randint(1, 30)
        b.append(n)
    print(str(b))
    # create a function to remove duplicates from the product of the first two-random-list function
    remove_duplicates_a = []
    for i in a:
        if i not in remove_duplicates_a:
            remove_duplicates_a.append(i)
    remove_duplicates_b = []
    for i in b:
        if i not in remove_duplicates_b:
            remove_duplicates_b.append(i)
    for element in remove_duplicates_a:
        if element in remove_duplicates_b:
            print(element)
    #else:
        #print("No overlapping values in the lists.")

list_overlap()