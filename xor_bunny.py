def answer(start, length):
    # your code here
    answer=0
    #test=[start]
    for i in xrange(length, 0, -1):
      answer ^= (truth(start+i-1)^truth(start-1))
      start+=length
        
    return answer
    
def truth(n):
    table = [n, 1, n+1, 0]
    return table[n%4]
