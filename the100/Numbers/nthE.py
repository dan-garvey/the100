import math
from math import*

def getInput():
    digits=int(input())
    if digits>47:
        print('try again, less than 48')
        return getInput()
    return digits

print("How many digits of e would you like? (Maximum 47)")
dig= getInput()
f='%.48f' % math.e
print(str(f[:dig+2]))
