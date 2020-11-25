"""
Write a program which accept number from user and print even factors of that
number.
Input : 36
Output: 2 6 12 18
"""
import sys

def DispEvenFact(No):
    i = 2
    if No <= 0:
        No = -No
    while(i <= No/2):
        if i%2 == 0 & No%i == 0:
            print(i,end = " ")
        i += 1

No = int(input("Enter Number :"))
DispEvenFact(No)
