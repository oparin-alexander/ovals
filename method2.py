import random
import geometry
import matplotlib.pyplot as plt


DELTA_POINTS = 30

'''
print(wurf)
aaa = [crossPoint[0], points[k][0], points[k1][0], hordPoint[0]]
bbb = [crossPoint[1], points[k][1], points[k1][1], hordPoint[1]]
plt.plot(aaa, bbb, 'r.')
plt.show()
'''


def findPair(points, k, crossPoint, i1, i2):
    global NUM_POINTS
    minDelta=10000.0
    kOpt = 0


    k1 = (i2 + DELTA_POINTS)%NUM_POINTS
    while k1 != (NUM_POINTS + i1-DELTA_POINTS) % NUM_POINTS:
        delta = geometry.line2pointDist((crossPoint,points[k]), points[k1])
        if delta <= minDelta:
            minDelta = delta
            kOpt = k1
        '''
        else:
            return kOpt
        '''
        k1= (k1 + 1) % NUM_POINTS

    if minDelta >10:
        return None
    else:
        return kOpt


def iterateCross(points, i1, i2, crossPoint):
    global NUM_POINTS

    minDelta=10000.0
    optimalPoint =()

    bbb=[]
    k= (i1 + DELTA_POINTS)%NUM_POINTS
    while k != (NUM_POINTS + i2-DELTA_POINTS)%NUM_POINTS:
        k1 = findPair(points, k, crossPoint, i1, i2)
        if k1 == None:
            k = (k + 1) % NUM_POINTS
            continue

        hordPoint = geometry.line2line2((points[i1], points[i2]), (crossPoint, points[k1]))
        if hordPoint==None:
            k= (k + 1) % NUM_POINTS
            continue

        wurf = geometry.wurf(crossPoint, points[k], hordPoint, points[k1])
        deltaWurf = abs(wurf-2)
        #bbb.append(deltaWurf)

        if deltaWurf < minDelta and deltaWurf<0.05:
            minDelta = deltaWurf
            optimalPoint = hordPoint
        k= (k + 1) % NUM_POINTS
    '''
    aaa = range(0, len(bbb))
    print("{} {}".format(len(aaa), len(bbb)))
    plt.plot(aaa, bbb, '.')
    plt.savefig('./temp/foo{}_{}.png'.format(i1, i2))
    '''

    if minDelta>2:
        return None
    else:
        return optimalPoint




def iterateHords(points, i):
    global NUM_POINTS
    a1, a2, curr, b1, b2  = points[i-2], points[i-1], points[i], points[(i+1)%len(points)], points[(i+2)%len(points)]
    tan1 = geometry.tangent(a1, a2, curr, b1, b2)

    optimalPoints = []

    opposite = (i + NUM_POINTS/2)%NUM_POINTS
    wind = 15
    for k in range(opposite-wind, opposite + wind):
        j = k%NUM_POINTS
        c1, c2, pair, d1, d2 = points[j - 2], points[j - 1], points[j], points[(j + 1) % NUM_POINTS], points[(j + 2) % NUM_POINTS]
        tan2 = geometry.tangent(c1, c2, pair, d1, d2)
        crossPoint = geometry.line2line(tan1, tan2)
        if crossPoint == None:
            continue
        optPoint = iterateCross(points, i, j, crossPoint)
        if (optPoint != () and optPoint != None):
            optimalPoints.append(optPoint)


    return optimalPoints


NUM_POINTS=300
def start(points):
    global NUM_POINTS
    NUM_POINTS = len(points
                     )
    optimalPoints = []
    pointis = []
    for i in range(0,4):
        print(i)
        point_i = random.randint(0, len(points)-1)
        optimalPoints.append(iterateHords(points, point_i))
        pointis.append(point_i)
    return optimalPoints, pointis