price=input('enter a dollar amount')
tax=input('enter tax amount as a percent')
if tax.isdecimal():
    res=float(price)+(float(tax)*float(price)/100)
else:
    res=float(price)+(float(tax.rstrip('%'))*float(price)/100)
print('Total is $%.2f' % res)
