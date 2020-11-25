"""
Write a program which accept number from user and print even factors of that
number.
Input : 24
Output: 1 2 4 6 8 12
"""
import sys

def DisplayFactor(No):
    i = 1
    while(i <= No/2):
        if No%i == 0:
            print(i,end = " ")
        i += 1

No = int(input("Enter Number :"))
DisplayFactor(No)
