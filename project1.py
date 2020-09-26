# assigning each character a binary code

def findcode(my_char):
    global code
    if my_char == "A":
        code = "0000000"
    elif my_char == "B":
        code = "0000001"
    elif my_char == "C":
        code = "0000010"
    elif my_char == "D":
        code = "0000100"
    elif my_char == "E":
        code = "0001000"
    elif my_char == "F":
        code = "0010000"
    elif my_char == "G":
        code = "0100000"
    elif my_char == "H":
        code = "0000011"
    elif my_char == "I":
        code = "0000111"
    elif my_char == "J":
        code = "0001111"
    elif my_char == "K":
        code = "0011111"
    elif my_char == "L":
        code = "0111111"
    elif my_char == "M":
        code = "0110000"
    elif my_char == "N":
        code = "0111000"
    elif my_char == "O":
        code = "0111100"
    elif my_char == "P":
        code = "0111110"
    elif my_char == "Q":
        code = "0101010"
    elif my_char == "R":
        code = "0011001"
    elif my_char == "S":
        code = "0011101"
    elif my_char == "T":
        code = "0100011"
    elif my_char == "U":
        code = "0100001"
    elif my_char == "V":
        code = "0100111"
    elif my_char == "W":
        code = "0101000"
    elif my_char == "X":
        code = "0101100"
    elif my_char == "Y":
        code = "0110011"
    elif my_char == "Z":
        code = "0111011"
    elif my_char == "the":
        code = "1010"
    elif my_char == "hello":
        code = "0100010"
    elif my_char == "goodbye":
        code = "0110100"
    elif my_char == "is":
        code = "0000110"
    elif my_char == "it":
        code = "0001101"
    elif my_char == "that":
        code = "0011100"
    elif my_char == "name":
        code = "0110010"
    elif my_char == "to":
        code = "0001011"
    elif my_char == "too":
        code = "0001010"
    elif my_char == "dog":
        code = "0011000"
    elif my_char == "cat":
        code = "1001011"
    elif my_char == "seem":
        code = "0110001"
    elif my_char == "take":
        code = "1001010"
    elif my_char == ".":
        code = "1111"
    elif my_char == "-":
        code = "1110"
    elif my_char == "!":
        code = "1101"
    elif my_char == "''":
        code = "1011"
    elif my_char == "":
        code = "1001"
    elif my_char == "/n":
        code = "1100"
    elif my_char == "a":
        code = "0000101"
    elif my_char == "b":
        code = "0101001"
    elif my_char == "c":
        code = "0110101"
    elif my_char == "d":
        code = "0010110"
    elif my_char == "e":
        code = "0111001"
    elif my_char == "f":
        code = "0010011"
    elif my_char == "g":
        code = "0011010"
    elif my_char == "h":
        code = "0100101"
    elif my_char == "i":
        code = "0101101"
    elif my_char == "j":
        code = "0010010"
    elif my_char == "k":
        code = "0111010"
    elif my_char == "l":
        code = "0100100"
    elif my_char == "m":
        code = "0011110"
    elif my_char == "n":
        code = "0101011"
    elif my_char == "o":
        code = "0101111"
    elif my_char == "p":
        code = "0010100"
    elif my_char == "q":
        code = "0001100"
    elif my_char == "r":
        code = "0100110"
    elif my_char == "s":
        code = "0101110"
    elif my_char == "t":
        code = "0011011"
    elif my_char == "u":
        code = "0111101"
    elif my_char == "v":
        code = "0010111"
    elif my_char == "w":
        code = "0010001"
    elif my_char == "x":
        code = "0110110"
    elif my_char == "y":
        code = "0001001"
    elif my_char == "z":
        code = "0010101"
    return code
