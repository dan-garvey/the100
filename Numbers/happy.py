def gethappy(num):
    if num==0 or num==2 or num==4:
        return False
    if num==1:
        return True
    else:
        string=str(num)
        total=0
        for x in string:
            try:
                total=total+int(x)**2
            except ValueError:
                return False
        #print('total currently:',total)
        return gethappy(total)
arehappy=[]
for x in range(10000):
    if gethappy(x):
        arehappy.append(x)
print(arehappy)
