import time

import oval
import matplotlib.pyplot as plt
import method
import method2



x = []
y = []

def main():
    startT = time.time()
    global x, y
    rsOval = oval.generate2(100, 50, 300)
    #rsOval = oval.proect(rsOval, 5,4,2, 2,3,2, 0,0,1)

    for point in rsOval:
        pX, pY = point
        x.append(pX)
        y.append(pY)

    optPoints, ipoints = method2.start(rsOval)

    x1=[]
    y1=[]
    i = 0
    for stack in optPoints:
        x1.append([])
        y1.append([])
        for point in stack:
            pX, pY = point
            x1[i].append(pX)
            y1[i].append(pY)
        i +=1

    finishT = time.time()

    print "{} s".format(finishT - startT)
    plt.plot(x, y, 'b-', x1[0], y1[0], 'r-', x1[1], y1[1], 'g-', x1[2], y1[2], 'c-', x1[3], y1[3], 'm-')


    plt.show()


if __name__ == "__main__":
    main()