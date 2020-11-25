"""
Write a program which accept one number from user and print that number of even numbers on screen.
Input : 7
Output: 2 4 6 8 10 12 14
"""
import sys

def DisplayEven(No):
    i = 1
    while(i <= No*2):
        if i%2 == 0:
            print(i,end = " ")
        i += 1

No = int(input("Enter Number :"))
DisplayEven(No)
