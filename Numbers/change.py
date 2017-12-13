print('Cost?')
cost=float(input())
print('Cash paid?')
cash=float(input())
change='%.2f'%(cash-cost)
dnc=change.split('.')
dollars=int(dnc[0])
cents=int(dnc[1])

hundreds=dollars//100
fifties=dollars%100//50
twenties=dollars%50//20
tens=dollars%50%20//10
fives=dollars%10//5
ones=dollars%5
quarters=cents//25
dimes=cents%25//10
nickels=cents%25%10//5
pennies=cents%5
print('Your change is: $'+change)
print('Hundreds:',hundreds,'\nFifties:',fifties,'\nTwenties:',twenties,
        '\nTens:',tens,'\nFives:',fives,'\nOnes:',ones)
print('Quarters:',quarters,'\nDimes:',dimes,'\nNickels:',nickels,'\nPennies:',
        pennies)
