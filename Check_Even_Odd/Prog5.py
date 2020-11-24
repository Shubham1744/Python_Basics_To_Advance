# Accept number from user and check whether number is even or odd.

def ChkEven(No):
    if No <= 0:
        return False

    if No%2 == 0:
        return True
    else:
        return False

No = int(input("Enter Number :"))
bret = ChkEven(No)

if bret == True:
    print("it is even")
else:
    print("it is not even")
