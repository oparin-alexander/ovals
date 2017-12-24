import time

import oval
import matplotlib.pyplot as plt
import sys
import method2

x = []
y = []

#5 4 2  2 3 2  0 0 1
#3 4 2  2 3 2  0 0 1
def main():
    print sys.argv
    startT = time.time()
    global x, y
    rsOval = oval.generate2(100, 50, 600)
    initialCenter = [(25, 0)]


    if len(sys.argv) >= 10:
        t, c1, c2, c3, c4, c5, c6, c7, c8, c9 = sys.argv
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = int(c1), int(c2), int(c3), int(c4), int(c5), int(c6), int(c7), int(c8), int(c9)
        rsOval = oval.proect(rsOval, c1, c2, c3, c4, c5, c6, c7, c8, c9)
        initialCenter = oval.proect(initialCenter, c1, c2, c3, c4, c5, c6, c7, c8, c9)

    for point in rsOval:
        pX, pY = point
        x.append(pX)
        y.append(pY)

    optPoints, i_s, center = method2.start(rsOval)

    x1 = []
    y1 = []
    i = 0
    for stack in optPoints:
        x1.append([])
        y1.append([])
        for point in stack:
            pX, pY = point
            x1[i].append(pX)
            y1[i].append(pY)
        i += 1

    finishT = time.time()

    print "{} s".format(finishT - startT)
    plt.plot(x, y, 'b-', [initialCenter[0][0]], [initialCenter[0][1]], 'b.',
             x1[0], y1[0], 'r,', x1[1], y1[1], 'g,', x1[2], y1[2], 'c,', x1[3], y1[3], 'm,',
             rsOval[i_s[0]][0], rsOval[i_s[0]][1], 'r.', rsOval[i_s[1]][0], rsOval[i_s[1]][1], 'g.', rsOval[i_s[2]][0],
             rsOval[i_s[2]][1], 'c.', rsOval[i_s[3]][0], rsOval[i_s[3]][1], 'm.',
             [center[0]], [center[1]], 'r.')

    plt.show()


if __name__ == "__main__":
    main()
