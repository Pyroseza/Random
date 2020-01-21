#!/usr/bin/env python3
import string

def rotate(message, key):
    translated = ""
    for symbol in message:
        if symbol.isalpha():
            letters = string.ascii_uppercase
            if symbol.islower():
                letters = string.ascii_lowercase
            num = letters.index(symbol)
            num += key
            num = num % len(letters)
            symbol = letters[num]
        translated += symbol
    return translated
print(rotate("the SECRET message",13))
print(rotate("gur FRPERG zrffntr",13))
