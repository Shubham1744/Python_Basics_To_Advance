"""
Accept one character from user and convert case of that character.
Input : a Output : A
Input : D Output : d
"""

import sys

def DisplayConvert(ch):
    if (ch >= "A") & (ch <= "Z"):
        result = ord(ch) + 32
        print(chr(result))
    elif (ch >= "a") & (ch <= "z"):
        result = ord(ch) - 32
        print(chr(result))
    else:
        print("No letter found")

ch = input("Enter character :")
DisplayConvert(ch)
