def answer(versions):
  #sorts a list of version numbers (X.Y.Z) in 
  ans = []
  for item in test1:
    temp = 0
    split = item.split('.')
    for i in range(len(split)):
      temp += int(split[i]*10**(3-i))
    ans.append((temp, item))
  ans = [item for temp, item in sorted(ans)]
  return ans
