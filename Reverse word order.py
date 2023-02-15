def reverse_word_order():
    user_string = input("Please write a sentence: ")
    words = user_string.split(" ")
    nacho = words[len(words):: -1]  # iterating backwards from total length of words with step -1
    nacho = " ".join(nacho)  # joining elements of list "nacho" with a space " " and therefore making it to a string
    print(nacho)
    words.reverse()  # using list.reverse() function to reverse word list
    reversed_words = " ".join(words)
    print(reversed_words)


reverse_word_order()
