def karatsuba(x, y):
  #algorithm for doing integer multiplication
  x=str(x)
  y=str(y)
  m = max(len(x), len(y))
  m2 = m//2
  if min(len(x),len(y))==1:
    return int(x)*int(y)
  b = int(x[-m2:])
  d = int(y[-m2:])
  a = int(x[:-m2])
  c = int(y[:-m2])
  z0 = karatsuba(a,c)
  z2 = karatsuba(b,d)
  z1 = karatsuba((a+b), (c+d))
  return int((10**(m2*2))*z0 + 10**(m2)*(z1-z2-z0)+z2)
  
