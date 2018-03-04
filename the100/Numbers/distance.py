from math import*

def getInput():
    print('Please type longitude and latitude for the first coordinate, seperate with comma')
    coord1=str(input()).split(',')
    print('Please type longitude and latitude for the second coordinate, seperate with comma')
    coord2=str(input()).split(',')
    return coord1, coord2
def calcDist(pointa, pointb):
    alat=radians(float(pointa[0]))
    blat=radians(float(pointb[0]))
    difflon=radians(float(pointb[1])-float(pointa[1]))
    R=6731000
    distance= acos(sin(alat)*sin(blat)+cos(alat)*cos(blat)*cos(difflon))*6731000
    return distance

def haversine(p1,p2):
    ru=6371
    lat1=radians(float(p1[1]))
    lat2=radians(float(p2[1]))
    diflat=radians(float(p2[1])-float(p1[1]))
    diflon=radians(float(p2[0])-float(p1[0]))
    forgetgeometry=sin(diflat/2)*sin(diflat/2)+cos(lat1)*cos(lat2)*sin(diflon/2)*sin(diflon/2)
    serious=2*atan2(sqrt(forgetgeometry), sqrt(1-forgetgeometry))
    return ru*serious
c1, c2= getInput()
print('distance is:',haversine(c1,c2),'km.')
