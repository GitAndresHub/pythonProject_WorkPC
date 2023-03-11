def ask_name_and_greet_user():
    name = input("What is your name?").casefold()
    if name == "thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        print("Hi, " + name.capitalize() + ". Would you like to have a Hamburger?")
#    return ask_name_and_greet_user()


print(ask_name_and_greet_user())
