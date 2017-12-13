import math
from math import*

def isPrime(num):
    if num%2==0 or num%3==0:
        return False
    for n in range(5, int(num**(1/2))):
        if num%n==0:
            return False
    return True

print('enter a positive integer')
FacMe=int(input())
primefacts=[1]
if not isPrime(FacMe):
    if FacMe % 2==0:
        primefacts.append(2)
    if FacMe % 3==0:
        primefacts.append(3)
    for i in range(5,FacMe):
        if FacMe%i==0:
            if isPrime(i):
                primefacts.append(i)
else:
    primefacts.append(FacMe)
print(primefacts)
