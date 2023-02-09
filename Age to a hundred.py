def tell_year_when_hundred():

    give_name = input("Please enter your name: ")
    give_age = input("Please enter your age: ")
    how_many_times = input("How many times would you like to see the next message? ")
    age = int(give_age)
    times = range(int(how_many_times))
    when_hundred = 2023 - age + 100
    for i in times:
        print(f"You, {give_name}, will turn a hundred years old on year {when_hundred}.")

tell_year_when_hundred()