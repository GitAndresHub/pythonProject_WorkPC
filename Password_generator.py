import random
import string


def generate_password():
    instructions = input("How many characters do you want in your password?")
    char_num = int(instructions)
    password = []
    i = 0
    while i <= char_num:
        char = random.choice(string.ascii_letters)
        num = random.randint(0, 9)
        password = str(char + str(num))
        print(password)
        password = list(password)
        print(password)
        password = password.append(password)
        i += 1
        print(password)


generate_password()