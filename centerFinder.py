import numpy as np
import matplotlib.pyplot as plt

def generateXarray(optimalPoints):
    allX = []
    px = []
    py = []
    for pArrI in optimalPoints:
        xTemp = []
        yTemp = []
        pArr = sorted(pArrI, key=lambda p: p[0])
        for i in range(1, len(pArr)-1):
            xTemp.append(pArr[i][0])
            yTemp.append(np.mean([pArr[i-1][1], pArr[i][1], pArr[i+1][1]]))
            allX.append(pArr[i][0])
        px.append(xTemp)
        py.append(yTemp)

    allX = list(set(allX))
    allX = np.linspace(np.min(allX), np.max(allX), num=1000, endpoint=True)
    #allX = sorted(allX)
    return allX, px, py


def find(optimalPoints):
    print "get all x"
    allX, px, py = generateXarray(optimalPoints)
    print allX
    print "interpl"
    f = []
    for i in range(0, len(optimalPoints)):
        f.append(np.interp(allX, px[i], py[i]))

    print"find center"
    minDelta = 1000
    allCx = []
    allCy = []
    for j in range(0, 4):
        f1, f2, f3, f4 = f[j% len(optimalPoints)], f[(1+j)% len(optimalPoints)], f[(2+j)% len(optimalPoints)], f[(3+j)% len(optimalPoints)]
        for i in range(0, len(allX)-1):
            print i
            delta = np.max([f1[i], f2[i], f3[i], f4[i]]) - np.min([f1[i], f2[i], f3[i], f4[i]])
            if delta < minDelta:
                minDelta = delta
                cx = allX[i]
                cy = np.mean([f1[i], f2[i], f3[i], f4[i]])
        allCx.append(cx)
        allCy.append(cy)
    return np.mean(allCx), np.mean(allCy)

