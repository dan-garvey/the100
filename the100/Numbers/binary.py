def toBinary(num):
    result=''
    g=num
    while(g>0):
        result= str(g%2)+result
        g=g//2
    return result
def toBaseTen(num):
    g=str(num)
    exp=0
    result=0
    for i in range(len(g)-1,-1,-1):
        print(int(g[i]))
        result+=(int(g[i])*2**exp)
        exp+=1
    return result


print('Convert what number to binary?')
x=toBinary(int(input()))
print(x)
print(toBaseTen(x))
