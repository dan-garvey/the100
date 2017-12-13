from math import*
from operator import itemgetter
import random as ra
def dist(p1,p2):
    return sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
def minCheck(pointsByX):
    mindist=dist(pointsByX[0],pointsByX[1])
    for i in range(len(pointsByX)):
        for j in range(len(pointsByX)):
            if not i==j:
                tdist=dist(pointsByX[i],pointsByX[j])
                if mindist> tdist:
                    mindist= tdist
    return mindist
def subcheck(pointsByX):
    lpts=pointsByX[len(pointsByX)//2:]
    rpts=pointsByX[:len(pointsByX)//2]
    lmin=minCheck(lpts)
    rmin=minCheck(rpts)
    return min(lmin,rmin)
def middleCheck(pointsByX, submin):
    strip=[]
    midline = pointsByX[len(pointsByX)//2][0]
    for x in range(len(pointsByX)):
        if abs(pointsByX[x][0]-midline)<submin:
            strip.append(pointsByX[x])
    if len(strip)>1:
        return min(submin, minCheck(strip))
    return submin
testpoints=[]
for i in range(30):
    testpoints.append((ra.randint(-100,100),ra.randint(-100,100)))
#print(testpoints)
testpoints.sort(key=itemgetter(0))
print(testpoints)

print(middleCheck(testpoints, subcheck(testpoints)))
print(minCheck(testpoints))
