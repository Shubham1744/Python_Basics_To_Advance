"""
Accept on character from user and check whether that character is vowel
(a,e,i,o,u) or not.
Input : E Output : TRUE
Input : d Output : FALSE
"""

def ChkVowel(ch):
    if (ch == 'a')|(ch == "e")|(ch == "i")|(ch == "o")|(ch == "u")|(ch == "A")|(ch == "E")|(ch == "I")|(ch == "O")|(ch == "U"):
        return True
    else:
        return False

ch = input("Enter character :")
bret = ChkVowel(ch)
if bret == True:
    print("It is Vowel")
elif bret == False:
    print("It is not a vowel")
