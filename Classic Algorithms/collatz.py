def collatz(num):
    count=0
    mod=num
    while(not mod==1):
        if mod%2==0:
            mod=mod/2
        else:
            mod=mod*3+1
        count+=1
    return count
test=[2,4,10,17,33,46,1004,24758189]
for x in test:
    print('collatz of '+str(x)+':',collatz(x))
