#Program to divide two numbers

def Divide(No1,No2):
    if No2 == 0 :
        return -1
    return No1/No2;

No1 = float(input("Enter First Number :"))
No2 = float(input("Enter Second Number :"))
iAns = Divide(No1,No2)
print("Division is :",iAns);
