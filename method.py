import random
import geometry
import matplotlib.pyplot as plt


DELTA_POINTS = 70

'''
print(wurf)
aaa = [crossPoint[0], points[k][0], points[k1][0], hordPoint[0]]
bbb = [crossPoint[1], points[k][1], points[k1][1], hordPoint[1]]
plt.plot(aaa, bbb, 'r.')
plt.show()
'''


def findPair(points, k, crossPoint, i1, i2):
    minDelta=10000.0
    kOpt = 0
    delta = 10000.0
    numPoint = len(points)


    k1 = (i2 + DELTA_POINTS)%numPoint
    while k1 != (numPoint + i1-DELTA_POINTS) % numPoint:
        delta = geometry.line2pointDist((crossPoint,points[k]), points[k1])
        if delta <= minDelta:
            minDelta = delta
            kOpt = k1
        '''
        else:
            return kOpt
        '''
        k1= (k1 + 1) % numPoint

    if minDelta >10:
        return None
    else:
        return kOpt


def isIncenterHord(points, i1, i2, hordPoint):
    x1, y1 = points[i1]
    x2, y2 = points[i2]
    xc, yc = hordPoint


def iterateCross(points, i1, i2, crossPoint):
    numPoint = len(points)

    minDelta=10000.0
    optimalPoint =()

    k= (i1 + DELTA_POINTS)%numPoint
    while k != (numPoint + i2-DELTA_POINTS)%numPoint:
        k1 = findPair(points, k, crossPoint, i1, i2)
        if k1 == None:
            k = (k + 1) % numPoint
            continue

        hordPoint = geometry.line2line2((points[i1], points[i2]), (crossPoint, points[k1]))
        if hordPoint==None:
            k= (k + 1) % numPoint
            continue

        wurf = geometry.wurf(crossPoint, points[k], hordPoint, points[k1])
        deltaWurf = abs(wurf-2)

        if deltaWurf < minDelta :
            minDelta = deltaWurf
            optimalPoint = hordPoint
        k= (k + 1) % numPoint

    if minDelta>2:
        return None
    else:
        return optimalPoint




def iterateHords(points, i):
    a1, a2, curr, b1, b2  = points[i-2], points[i-1], points[i], points[(i+1)%len(points)], points[(i+2)%len(points)]
    tan1 = geometry.tangent(a1, a2, curr, b1, b2)
    numPoints = len(points)

    optimalPoints = []
    aaa = []
    bbb = []
    j = (i + DELTA_POINTS) % numPoints
    while j!= (i - DELTA_POINTS) % numPoints:
        c1,c2, pair, d1, d2 = points[j-2], points[j-1], points[j], points[(j+1)%numPoints], points[(j+2)%numPoints]
        tan2 = geometry.tangent(c1, c2, pair, d1, d2)
        crossPoint = geometry.line2line(tan1, tan2)
        if crossPoint == None:
            j = (j+1)%numPoints
            continue
        optPoint = iterateCross(points, i, j, crossPoint)
        if(optPoint!=() and optPoint!=None):
            optimalPoints.append(optPoint)
        j = (j+1)%numPoints

    return optimalPoints



def start(points):
    optimalPoints = []
    pointis = []
    for i in range(0,4):
        print(i)
        point_i = random.randint(0, len(points)-1)
        optimalPoints.append(iterateHords(points, point_i))
        pointis.append(point_i)

    print(len(optimalPoints[0]), len(optimalPoints[1]), len(optimalPoints[2]), len(optimalPoints[3]))
    return optimalPoints, pointis