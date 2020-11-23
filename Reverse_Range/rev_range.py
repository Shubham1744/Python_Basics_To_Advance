# Program to print 5 to 1 numbers on screen.

def DispRev(int n):
    for i in range(n,0,-1):     #range(start,stop,increment/decrement)
        print(i)

n = int(input("Enter Number"))
DispRev()
