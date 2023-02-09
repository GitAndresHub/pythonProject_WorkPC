
def ask_user_age(age_limit: int) -> int:
    """
    Ask user age.

    You have to ask the user his/her age using input("What is your age?").
    You have to repeat this process until a correct age is entered.
    The age is correct if:
    - it is numeric (answering "a" is not correct)
    - it is greater or equal to the age_limit
    - it is less or equal to 100

    So, if the user enters a wrong age, the user gets a warning.
    The question is repeated until a correct age is entered.
    The function returns the correct age as int.

    Warning is printed out:
    - non numberic input: Wrong input!
    - age < age_limit: Too young!
    - age > 100: Too old!

    An example (with age_limit 18):
    What is your age? a
    Wrong input!
    What is your age? 10
    Too young!
    What is your age? 101
    Too old!
    What is your age? 21

    (function returns 21)
    """

    while True:
        age = input("What is your age?")
        if age.isnumeric():  # checking if input provided is number
            agenr = int(age)  # if numbers provided, converting the string to integer
            if agenr > 100:  # if the number higher than 100, print "Too old!"
                print("Too old!")
            elif agenr >= age_limit:  # if age provided is equal or larger than the set limit, print the age
                return int(age)
            elif agenr < age_limit:  # if age smaller than set limit, print "Too young!"
                print("Too young!")
        else:
            print("Wrong input!")  # if anything else than number provided as input, print "Wrong input!"

print(ask_user_age(18))


