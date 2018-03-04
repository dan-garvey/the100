def sort(list):
    isSorted=False
    revInd=1
    while not isSorted:
        isSorted=True
        for i in range(len(list)-revInd):
            if list[i]>list[i+1]:
                swap=[list[i+1],list[i]]
                list[i], list[i+1] =swap
                isSorted=False
        revInd+=1
    return list
tests=[[5,4,3,2,1,0],[4,6,33,54,6,4,3,1,5,6,3,4,5,6], [2,5,6,3,521,5,6,2,4,5,6,77]]
for a in tests:
    sort(a)
    print(a)
