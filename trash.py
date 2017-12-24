def findPair(points, k, crossPoint, i1, i2):
    global NUM_POINTS
    minDelta = 10000.0
    kOpt = 0

    k1 = (i2 + DELTA_POINTS) % NUM_POINTS

    for k1  in range( i1 % NUM_POINTS, i2%NUM_POINTS, -1):
        delta = geometry.line2pointDist((crossPoint, points[k]), points[k1])
        if delta <= minDelta:
            minDelta = delta
            kOpt = k1
        '''
        else:
            return kOpt
        '''

    if minDelta > 10:
        return None
    else:
        return kOpt


def iterateCross(points, i1, i2, crossPoint):
    global NUM_POINTS

    minDelta = 10000.0
    optimalPoint = ()
    bbb = []

    if abs(i2 - i1) < abs(i1 - i2):
        i1, i2 = i2, i1
    avr = (i2 - i1) / 2
    win = 100

    for v in range(avr - win, avr + win):
        k = v % NUM_POINTS
        k1 = findPair(points, k, crossPoint, i1, i2)
        if k1 == None:
            continue

        hordPoint = geometry.line2line2((points[i1], points[i2]), (crossPoint, points[k1]))
        if hordPoint == None:
            continue

        wurf = geometry.wurf(crossPoint, points[k], hordPoint, points[k1])
        deltaWurf = abs(wurf - 2)
        # bbb.append(deltaWurf)
        if deltaWurf < minDelta and deltaWurf < 0.05:
            minDelta = deltaWurf
            optimalPoint = hordPoint
    '''
    aaa = range(0, len(bbb))
    print("{} {}".format(len(aaa), len(bbb)))
    plt.plot(aaa, bbb, '.')
    plt.savefig('./temp/foo{}_{}.png'.format(i1, i2))
    '''

    if minDelta > 2:
        return None
    else:
        return optimalPoint