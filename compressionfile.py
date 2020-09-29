# import functions from file project1.py
from project1 import findcode

# open text file to read through
my_file = open("project1.py")

# assign the characters in the text file to the string my_string
my_string = my_file.read()

print(len(my_string))

# loop through all of the characters in the string to get their binary codes
    i = 0
    # using a while loop instead of a for loop to acommodate for the following words:
    while i < len(my_char) - 1:
        if my_char[i:i + 3] == "the":
            val = findcode(my_char[i:i + 3])
            print(my_char[i:i + 3], " ", val)
            i = i + 3
        if my_char[i:i + 5] == "hello":
            val = findcode(my_char[i:i + 5])
            print(my_char[i:i + 5], " ", val)
            i = i + 5
        if my_char[i:i + 7] == "goodbye":
            val = findcode(my_char[i:i + 7])
            print(my_char[i:i + 7], " ", val)
            i = i + 7
        if my_char[i:i + 2] == "is":
            val = findcode(my_char[i:i + 2])
            print(my_char[i:i + 2], " ", val)
            i = i + 2
        if my_char[i:i + 2] == "it":
            val = findcode(my_char[i:i + 2])
            print(my_char[i:i + 2], " ", val)
            i = i + 2
        if my_char[i:i + 4] == "that":
            val = findcode(my_char[i:i + 4])
            print(my_char[i:i + 4], " ", val)
            i = i + 4
        if my_char[i:i + 4] == "name":
            val = findcode(my_char[i:i + 4])
            print(my_char[i:i + 4], " ", val)
            i = i + 4
        if my_char[i:i + 2] == "to":
            val = findcode(my_char[i:i + 2])
            print(my_char[i:i + 2], " ", val)
            i = i + 2
        if my_char[i:i + 3] == "too":
            val = findcode(my_char[i:i + 3])
            print(my_char[i:i + 3], " ", val)
            i = i + 3
        if my_char[i:i + 3] == "dog":
            val = findcode(my_char[i:i + 3])
            print(my_char[i:i + 3], " ", val)
            i = i + 3
        if my_char[i:i + 3] == "cat":
            val = findcode(my_char[i:i + 3])
            print(my_char[i:i + 3], " ", val)
            i = i + 3
        if my_char[i:i + 4] == "seem":
            val = findcode(my_char[i:i + 4])
            print(my_char[i:i + 4], " ", val)
            i = i + 4
        if my_char[i:i + 4] == "take":
            val = findcode(my_char[i:i + 4])
            print(my_char[i:i + 4], " ", val)
            i = i + 4
