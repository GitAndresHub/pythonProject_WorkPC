def palindrome_or_not():
    user_str = input("Please enter characters: ")
    reverse = (user_str[-1::-1])
    print("Forward direction: " + user_str)
    print("                   ", end="")
    for i in user_str:
        print("│", end="")
    print("\nReverse direction: " +  reverse)
    if user_str == reverse:
        print("We're dealing with a palindrome here!")
    else:
        print("This is not a palindrome.")
palindrome_or_not()