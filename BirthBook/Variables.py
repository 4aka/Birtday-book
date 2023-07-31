import os


class Variables:
    name_symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
                    '(', ')', '_', '-', '=', '+', '/', '\\',
                    '.', ',', '№', ';', '?', ':', '<', '>',
                    '[', ']', '{', '}', '\|', '0', '1', '2',
                    '3', '4', '5', '6', '7', '8', '9', '\'',
                    '\"', '~', '`', ' ', '\n']

    birth_symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
                     '(', ')', '_', '=', '+', '/', '\\', ',',
                     '№', ';', '?', ':', '<', '>', '[', ']',
                     '{', '}', '\|', '\\n']

    positive_answers = ['y', 'yes', 'Y', 'Yes', 'YES', '+']

    alphabetic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']

    integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    file = ROOT_DIR + '\\file_book.txt'

    try:
        open(file, "r").readable()
    except FileNotFoundError as e:
        open(file, "x")
