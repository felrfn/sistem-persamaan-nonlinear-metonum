import math

import numpy as np


def f1(x, y):
    return x**2 + x * y - 10


def f2(x, y):
    return y + 3 * x * y**2 - 57


def g1B(x, y):
    radicand = 10 - x * y
    if radicand < 0:
        return float("nan")
    return math.sqrt(radicand)


def g2B(x, y):
    if x == 0:
        return float("inf")
    radicand = (57 - y) / (3 * x)
    if radicand < 0:
        return float("nan")
    return math.sqrt(radicand)


def jacobian(x, y):
    df1_dx = 2 * x + y
    df1_dy = x
    df2_dx = 3 * y**2
    df2_dy = 1 + 6 * x * y
    return np.array([[df1_dx, df1_dy], [df2_dx, df2_dy]])
