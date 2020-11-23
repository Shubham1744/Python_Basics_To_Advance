# Accept one number and check whether is is divisible by 5 or not.

def CheckDivisible(No1):
    if No1 % 5 == 0:
        return True
    else:
        return False

No1 = int(input("Enter Number :"))
bret = CheckDivisible(No1)
if bret == True:
    print("divisible by 5")
else :
    print("Not divisible by 5")
