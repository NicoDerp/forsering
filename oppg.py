import matplotlib.pyplot as plt
import numpy as np


dx = 0.000001


def f(x):
    return 2*x**2 + 3*x - 2


def tangent(func, x):
    return (func(x+dx)-func(x))/dx


print(tangent(f, 3))

