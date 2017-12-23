import numpy as np


def derivative(a1, a2, c1, c2):
    a1x, a1y = a1
    a2x, a2y = a2
    c1x, c1y = c1
    c2x, c2y = c2
    return (
        (a1y + a2y - c1y - c2y) /
        (a1x + a2x - c1x - c2x)
    )


def tangent(a1, a2, current, c1, c2):
    cuX, cuY = current
    try:
        k = derivative(a1, a2, c1, c2)
    except ZeroDivisionError:
        return None
    else:
        b = cuY - k * cuX
        return (k, b)


def line2line(l1, l2):
    k1, b1 = l1
    k2, b2 = l2
    if k1-k2==0:
        return None
    x = -(b1 * 1.0 - b2) / (k1 - k2)
    y = k1 * x + b1
    return x, y


def distantion(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def wurf(p1, p2, p3, p4):
    if distantion(p1, p2) > distantion(p1, p4):
        p2, p4 = p4, p2
    a = distantion(p1, p2)
    b = distantion(p2, p3)
    c = distantion(p3, p4)

    return (a + b) * (b + c) / (b * (a + b + c))


def line2line2(l1, l2):
    p1, p2 = l1
    p3, p4 = l2

    p1x, p1y = p1
    p2x, p2y = p2
    p3x, p3y = p3
    p4x, p4y = p4

    a1, b1 = p2y - p1y, p2x - p1x
    a2, b2 = p4y - p3y, p4x - p3x
    M = [[a1, -b1],
         [a2, -b2]]
    v = [a1 * p1x - b1 * p1y, a2 * p3x - b2 * p3y]

    x, y = np.linalg.solve(M, v)

    return x, y


def line2pointDist(l, p):
    p1, p2 = l
    x1, y1 = p1
    x2, y2 = p2
    x, y = p

    A = y2 - y1
    B = x2 - x1
    C = x2*y1 - y2*x1

    d = abs(A * x - B * y + C * 1.0) / (A ** 2 + B ** 2) ** 0.5
    return d


def test():
    p = line2line2(((-7, -4), (-1, 2)), ((-6, 0), (-2, -2)))
    print p  # -4,-1

    p = line2line((1, 3), (-0.5, -3))
    print p  # -4,-1

    p = distantion((0, 4), (3, 0))
    print p  # 5

    w = wurf((0, 0), (3, 3), (5, 5), (9, 9))
    print w

    w1 = wurf((0, 0), (9, 9), (5, 5), (3, 3))
    print w1

    d = line2pointDist(((-1, 1), (2, -2)), (3, 3))
    print d


if __name__ == "__main__":
    test()
