import random


def guess_the_number():
    my_number = random.randint(1, 9)
    user = input("Pick a number from 1 to 9: ")
    if user.isnumeric():
        user_input = int(user)
    else:
        return print("Only numbers allowed!")
    while user_input > my_number:
        print("Too high!")
        user_input = int(input("Pick again: "))
    while user_input < my_number:
        print("Too low!")
        user_input = int(input("Pick again: "))
    while user_input == my_number:
        print("You guessed it!")
        user_input = int(input("Let's keep going, pick again!"))
    while user_input == "exit" or "Exit":
        return print("Quitting...")


guess_the_number()
