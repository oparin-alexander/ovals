import math
import numpy as np


def generate(a, b):
    points = []
    for x in range(0, b):
        y = (b**2 - (b-x)**2)**0.5
        points.append((x, y))
        points.append((a+b-x, -y))

    for x in range(b+1, b+a):
        y = b*(1 - ((x*1.0 - b)/a)**2)**0.5
        points.append((x, y))
        points.append((a+b-x, -y))
    return points



def generate2(a, b, num):
    #fis = range(0, 2*math.pi-0.0001, 2*math.pi/num)
    fis =    np.linspace(0, 2*math.pi, num=num, endpoint=False)
    points = []
    for fi in fis:
        nx = abs(math.cos(fi))
        ny = abs(math.sin(fi))
        if fi <= math.pi/2:
            points.append((nx*a, ny*b))
        elif fi <= math.pi:
            points.append((-nx*b, ny*b))
        elif fi <= 3.0/2*math.pi:
            points.append((a-b-nx*a, -ny*b))
        else:
            points.append((a-b+nx*b, -ny*b))

    return points
