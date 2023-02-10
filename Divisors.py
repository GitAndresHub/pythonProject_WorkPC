def divisors():
    number = input("Please provide a number (less than 10 billion) you want to find divisors for: ")
    my_number = int(number)
    x = range(1, (my_number + 1))
    for element in x:
        if my_number > 1000000000:
            return print("Too big number for calculations!")
        elif my_number % element == 0:
            print(element, end=" ")

divisors()