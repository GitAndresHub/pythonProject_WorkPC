def organise_by_first_symbol(strings: list) -> dict:

    # create an empty dictionary
    groups = {}

    # iterate over each word in the list
    for word in strings:
        # get the first letter of the word
        first_letter = word[0]
        # check if the first letter is already a key in the dictionary
        if first_letter in groups:
            # if it is, append the word to the list of words for that key
            groups[first_letter].append(word)
        else:
            # if it's not, create a new list with the word and add it to the dictionary
            groups[first_letter] = [word]

    # print the resulting dictionary
    print(groups)


organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"])