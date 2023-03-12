"""Dictionary exercises."""


def get_hobbies(hobbies_dict: dict, name: str) -> list:
    """
    Return the hobbies of a given person.

    hobbies = {
    "Tom": ["running", "reading"],
    "John": ["movies", "music", "swimming"]
    }

    get_hobbies(hobbies, "Tom")  => ["running", "reading"]
    get_hobbies(hobbies, "Timmy")  => "name not in dictionary"

    :param hobbies_dict: dictionary with peoples' hobbies.
    :param name: name of person whose hobbies are to be returned.

    :return: List of hobbies of the person with given name or "name not in dictionary".
    """
    if name in hobbies_dict:
        print(hobbies_dict[name])
    else:
        print("name not in dictionary")


get_hobbies({"Mart":["running", "sailing", "reading"], "Mari":["reading", "movies", "gossip"]}, "Mari")


def find_tallest(height_dict: dict) -> str:
    """
    Return the name of the tallest peron in given dictionary.

    find_tallest({"Tom": 186, "Mari": 175, "Jhon": 190}) => "Jhon"

    :param height_dict: dictionary with peoples' names and heights
    :return name of tallest person in given dict.
    """
    heights_max = max(list(height_dict.values()))
    for name, height in height_dict.items():
        if height == heights_max:
            print(name)


find_tallest({"Tom": 186, "Mari": 175, "Jhon": 190})


def remove_sixes(six_dict: dict) -> dict:
    """
    Return a dictionary where all keys which's values are dividable by six are removed.

    remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}) => {"a": 4, "b": 8}

    :param six_dict: dictionary to be modified.
    :return: dict without values that are dividable by six.
    """
    new_dict = {}
    for key, value in six_dict.items():
        if value % 6 != 0:
            new_dict[key] = value
    print(new_dict)



remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18})

def exchange_keys_and_values(exchange_dict: dict) -> dict:
    """
    Return a dict where keys and values have been exchanged.

    exchange_keys_and_values({"a": "b", "c": "d"}) => {"b": "a", "d": "c"}

    :param exchange_dict: dictionary to be modified.
    :return dictionary where values and keys have been exchanged.
    """
    new_dict = {}
    for key, value in exchange_dict.items():
        new_dict[value] = key
    print(new_dict)

exchange_keys_and_values({"a": "b", "c": "d"})
def count_symbol_appearances(stringy: str) -> dict:
    """
    Return dict where key is the symbol and the value is the count this symbol is present in the string.

    count_symbol_appearances("hello hi") => {'h': 2, 'e': 1, 'l': 2, 'o': 1, ' ': 1, 'i': 1}

    :param stringy: string to be processed.
    :return: dictionary with symbol counts.
    """
    new_dict = {}
    for element in stringy:
        value = stringy.count(element)
        key = element
        new_dict[key] = value
    print(new_dict)

count_symbol_appearances("hello hi")

def organise_by_first_symbol(strings: list) -> dict:
    """
    Return dict where key the is a symbol and the value is a list of words starting with this symbol.

    organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]) =>
        {'h': ['hello'], 'w': ['word', 'world', 'welcome'], 'y': ['yes']}

    :param strings: list of strings.
    :return: dict with starting symbol and corresponding words in order of appearance.
    """

    sorted = {}

    for element in strings:

        first = element[0]

        if first in sorted:

            sorted[first].append(element)

        else:
            sorted[first] = [element]

    print(sorted)
#    dictionary = {}  # create an empty dictionary
#
#   for element in strings:
#        key = element[0]
#        if key in dictionary:
#            dictionary[key].append(element)
#        else:
#            dictionary[key] = [element]
#    print(dictionary)


organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"])