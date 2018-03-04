print('How many fibonacci numbers do you want?')
N=int(input())
fibs=[0,1]
for i in range(N-2):
    fibs.append(fibs[i]+fibs[i+1])
print(fibs)
