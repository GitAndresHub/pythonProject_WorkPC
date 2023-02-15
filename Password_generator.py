import random
import string


def generate_password():
    instructions = int(input("How many characters do you want in your password? "))
    password = ()
    for i in range(instructions):
        while i <= instructions:
            char = random.choice(string.ascii_letters)
            num = random.randint(0, 9)
            spec = ["!", "#", "%", "&", "*", "@", "$", "£", "€"]
            special = random.choice(spec)
            ratio = random.randint(1, 10)
            if ratio < 5:
                password = char
            elif ratio > 8:
                password = str(special)
            else:
                password = str(num)
            i += 1
        print(password, end="")


generate_password()
