def isPrime(num):
    if num%2==0 or num%3==0 or num%5==0:
        return False
    for n in range(5, int(num**(1/2))):
        if num%n==0:
            return False
    return True

keepgoing=True
count =2
response=''
while keepgoing==True:
    if(isPrime(count)):
        print(count)
        print('Would you like the next prime? (y/n)')
        response=input()
        if response=='n':
            keepgoing=False
    count+=1
