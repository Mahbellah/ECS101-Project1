# import functions from file project1.py
from project1 import findcode

# open text file to read through
my_file = open("project1.py")

# assign the characters in the text file to the string my_string
my_string = my_file.read()

print(len(my_string))

# loop through all of the characters in the string to get their binary codes
for i in range(0, (my_char)):
    if my_char[i] == str:
        val = findcode(my_char)
        print(my_char[i], " ", val)
