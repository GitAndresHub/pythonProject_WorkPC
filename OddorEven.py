def odd_or_even():

    number = input("Please enter a number: ")
    check = input("Please enter a number to divide the first one: ")
    if number.isnumeric() and check.isnumeric():
        number = int(number)
        check = int(check)
        if number % check == 0:
            return print("Your second number divides evenly to the first one!")
        else:
            print("Your second number does not divide evenly to the first one!")
    else:
        print("Not a number!")

odd_or_even()
