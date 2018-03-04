n=int(input("Input an upper bound for n"))
primes=[False,False]
for i in range(2,n+1):
    primes.append(True)
for i in range(2, len(primes)):
    print("i=",i)
    if primes[i]:
        for j in range(i**2,len(primes),i):
            print('j=',j)
            primes[j]=False
    #print(i," ")
for i in range(0, len(primes)):
    if primes[i]:
        print(i)
