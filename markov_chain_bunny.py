def greatest_common_denominator(a,b):
    if not b==0:
        return greatest_common_denominator(b, a%b)
    return a
def list_denominators(inp):
    ans = 0
    size = len(inp)
    for i in range(size):
        ans = greatest_common_denominator(ans, inp[i])
    return ans
def backprop(a1, b1, a2, b2):
    ind = (set(range(len(a1)))-{b1,b2})
    tot = sum(a2)
    ans = [0 for i in a1]
    for i in ind:
        ans[i] = tot*a1[i]+a1[b2]*a2[i]
    greats = list_denominators(ans)
    print(ans)
    return [int(i/greats) for i in ans]
def answer(m):
    # your code here
    height = len(m)
    matrix = list(m)
    for i, node in enumerate(matrix):
        node[i] = 0
    totals = [sum(i) for i in matrix]
    terminating = [i for i,node in enumerate(totals) if node==0]
    nonterminating = list(set(range(height))-set(terminating))
    dist = len(nonterminating)
    
    for i in range(0,dist-1):
        inbetween = nonterminating[dist-i-1]
        for j in range(0, dist-1):
            inatween = nonterminating[j]
            matrix[inatween] = backprop(matrix[inatween], inatween, matrix[inbetween], inbetween)
    result = []
    for i in terminating:
        result.append(matrix[0][i])
    denom = sum(result)
    result.append(denom)
    if denom == 0:
        result= [1 for i in terminating]
        result.append(len(terminating))
    return result
