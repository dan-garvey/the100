print('How much does tile cost per sq/ft')
cost=float(input())
print('Width of floor in ft?')
w=float(input())
print('Length of floor in ft?')
l=float(input())
area=l*w
cost='%.2f'% (area*cost)

print('cost of floor is:$'+cost)
