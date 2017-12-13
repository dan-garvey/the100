print('how much is the loan in dollars?')
L=float(input())
print('what is the interest rate? Enter as percentage')
c=float(input())/100
print('How many payment periods?')
n=int(input())
P = L*((c*(1 + c)**n)/((1 + c)**n - 1))
print('$%.2f per month'% P )
