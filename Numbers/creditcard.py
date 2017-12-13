def getcard():
    print('please enter card number')
    card=str(input()).split(' ')
    return card
def luhn(card):
    reverse=''
    temp=''
    for z in card:
        reverse=z+reverse
    total=0
    for x in range(0, len(reverse)):
        if x==0 or x%2==0:
            temp=temp+reverse[x]
        else:
            temp=temp+str(int(reverse[x])*2)
    for y in temp:
        total=total+int(y)
    return total%10==0
testcard1='1234567890123452'
testcard2='4077142043835313'
testcard3='1234567890123453'
print('test 1 result=',luhn(testcard1))
print('test 2 result=',luhn(testcard2))
print('test 3 result=',luhn(testcard3))
