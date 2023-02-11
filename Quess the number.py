import random


def guess_the_number():
    my_number = random.randint(1, 9)
    user = input("Pick a number from 1 to 9: ")
    user_input = int(user)
    while user_input > my_number:
        print("Too high!")
        user_input = int(input("Pick again: "))
    while user_input < my_number:
        print("Too low!")
        user_input = int(input("Pick again: "))
    while user_input == my_number:
        return print("You guessed it!")


guess_the_number()
