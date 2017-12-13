def factorial(num):
    if not str(num).isdigit():
        return 'error, non-integer entered'
    if num<0:
        return 'error, negative number entered'
    if num>1:
        return num*factorial(num-1)
    else:
        return 1

def fact2(num):
    if not str(num).isdigit():
        return 'error, non-integer entered'
    if num==0:
        return 1
    if num<0:
        return 'error, incorrect entry'
    total=1
    for n in range(num,0,-1):
        total=total*n
    return total
testfactorials=[1,2,3,4,5,6,7,8,9,0, -4, .5, 'yo', ]
for x in testfactorials:
    print('test'+str(x)+'!:',factorial(x),fact2(x))
