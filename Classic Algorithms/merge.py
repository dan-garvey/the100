def sort(list):
    if len(list)<=1:
        return list
    else:
        left=sort(list[len(list)//2:])
        right=sort(list[:len(list)//2])
        return merge(left, right)
def merge(left,right):
    result=[]
    l,r=0,0
    lnr=len(left)+len(right)
    while len(result)<lnr:
        if left[l]>right[r]:
            result.append(right[r])
            if r<len(right)-1:
                r+=1
            else:
                result.extend(left[l:])
        else:
            result.append(left[l])
            if l<len(left)-1:
                l+=1
            else:
                result.extend(right[r:])
    return result
test1=sort([6,5,3,1,8,7,2,4])
print(test1)
