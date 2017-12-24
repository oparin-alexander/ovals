import random
import geometry
import matplotlib.pyplot as plt

DELTA_POINTS = 120


def findPair(points, k, crossPoint, i1, i2):
    minDelta = 10000.0
    kOpt = 0
    numPoint = len(points)

    k1 = (i2 + DELTA_POINTS) % numPoint
    while k1 != (i1 - DELTA_POINTS) % numPoint:
        delta = geometry.line2pointDist((crossPoint, points[k]), points[k1])
        if delta <= minDelta:
            minDelta = delta
            kOpt = k1
        elif minDelta < 10:
            return kOpt
        else:
            return None
        k1 = (k1 + 1) % numPoint

    if minDelta > 10:
        return None
    else:
        return kOpt


def iterateCross(points, i1, i2, crossPoint):
    minDelta = 10000.0
    optimalPoint = ()

    if i1 % NUM_POINTS > i2 % NUM_POINTS:
        i1, i2 = i2, i1

    for k in range((i1 + DELTA_POINTS) % NUM_POINTS, (i2 - DELTA_POINTS) % NUM_POINTS, 1):
        k1 = findPair(points, k, crossPoint, i1, i2)
        if k1 == None:
            continue

        hordPoint = geometry.line2line2((points[i1], points[i2]), (crossPoint, points[k1]))
        if hordPoint == None:
            continue

        wurf = geometry.wurf(crossPoint, points[k], hordPoint, points[k1])
        deltaWurf = abs(wurf - 2)

        if deltaWurf < minDelta:
            minDelta = deltaWurf
            optimalPoint = hordPoint

    if minDelta > 2:
        return None
    else:
        return optimalPoint


def iterateHords(points, i):
    a1, a2, curr, b1, b2 = points[i - 2], points[i - 1], points[i], points[(i + 1) % len(points)], points[
        (i + 2) % len(points)]
    tan1 = geometry.tangent(a1, a2, curr, b1, b2)

    optimalPoints = []

    opposite = (i + NUM_POINTS / 2) % NUM_POINTS
    wind = 30
    for k in range(opposite - wind, opposite + wind):
        j = k % NUM_POINTS
        c1, c2, pair, d1, d2 = points[j - 2], points[j - 1], points[j], points[(j + 1) % NUM_POINTS], points[
            (j + 2) % NUM_POINTS]
        tan2 = geometry.tangent(c1, c2, pair, d1, d2)
        crossPoint = geometry.line2line(tan1, tan2)
        if crossPoint == None:
            continue
        optPoint = iterateCross(points, i, j, crossPoint)
        if (optPoint != () and optPoint != None):
            optimalPoints.append(optPoint)

    return optimalPoints


NUM_POINTS = 300


def findCenter(optimalPoints):
    minDist = 1000
    e1, e2, e3, e4 = (0, 0, 0, 0)
    s=0
    for i in range(s, len(optimalPoints[0]) - 1 - s):
        print i
        for j in range(s, len(optimalPoints[1]) - 1 - s):
            for k in range(s, len(optimalPoints[2]) - 1 - s):
                for v in range(s, len(optimalPoints[3]) - 1 - s):
                    dist1 = geometry.distantion(optimalPoints[0][i], optimalPoints[1][j])
                    dist2 = geometry.distantion(optimalPoints[1][j], optimalPoints[2][k])
                    dist3 = geometry.distantion(optimalPoints[2][k], optimalPoints[3][v])
                    dist4 = geometry.distantion(optimalPoints[3][v], optimalPoints[0][i])
                    dist = dist1 + dist2 + dist3 + dist4
                    if dist < minDist:
                        minDist = dist
                        e1, e2, e3, e4 = optimalPoints[0][i], optimalPoints[1][j], optimalPoints[2][k], optimalPoints[3][v]
    print minDist
    return (e1[0] + e2[0] + e3[0] + e4[0]) / 4.0, (e1[1] + e2[1] + e3[1] + e4[1]) / 4.0


def start(points):
    global NUM_POINTS
    global DELTA_POINTS
    NUM_POINTS = len(points)
    DELTA_POINTS = int(NUM_POINTS * 0.2)
    optimalPoints = []

    firstPoint = random.randint(0, len(points) - 1)
    startPoints = [firstPoint]
    startPoints.append((firstPoint + 1 * NUM_POINTS / 4) % NUM_POINTS)
    startPoints.append((firstPoint + 2 * NUM_POINTS / 4) % NUM_POINTS)
    startPoints.append((firstPoint + 3 * NUM_POINTS / 4) % NUM_POINTS)
    for i in startPoints:
        print(i)
        optimalPoints.append(iterateHords(points, i))

    print(len(optimalPoints[0]), len(optimalPoints[1]), len(optimalPoints[2]), len(optimalPoints[3]))

    center = findCenter(optimalPoints)
    print center
    return optimalPoints, startPoints, center
