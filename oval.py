import math
import numpy as np


def generate2(a, b, num):
    fis = np.linspace(0, 2 * math.pi, num=num, endpoint=False)
    points = []
    for fi in fis:
        nx = abs(math.cos(fi))
        ny = abs(math.sin(fi))
        if fi <= math.pi / 2:
            points.append((nx * a, ny * b))
        elif fi <= math.pi:
            points.append((-nx * b, ny * b))
        elif fi <= 3.0 / 2 * math.pi:
            points.append((a - b - nx * a, -ny * b))
        else:
            points.append((a - b + nx * b, -ny * b))

    return points


def proect(points, c1, c2, c3, c4, c5, c6, c7, c8, c9):
    nPoints = []
    for point in points:
        x, y = point
        d = c7 * x + c8 * y + c9
        if d != 0:
            nx = (c1 * x + c2 * y + c3) * 1.0 / d
            ny = (c4 * x + c5 * y + c6) * 1.0 / d
            nPoints.append((nx, ny))
    return nPoints





def test():
    points = proect([(1,1)],1,1,1,1,1,1,1,1,1)
    print(points)


if __name__ == "__main__":
    test()