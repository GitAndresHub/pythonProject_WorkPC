def product_of_numbers():

    num_a = input("Please provide the first number: ")
    if num_a.isnumeric() != True:
        return ("Not a number!")
    num_b = input("Please provide the second number: ")
    if num_b.isnumeric() != True:
        return ("Not a number!")
    a_num = int(num_a)
    b_num = int(num_b)
    if a_num * b_num <= 1000:
        return (f"The product of given numbers is: {a_num * b_num}.")
    else:
        return (f"The sum of the given numbers is: {a_num + b_num}")

print(product_of_numbers())