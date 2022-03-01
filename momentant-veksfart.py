import matplotlib.pyplot as plt
import numpy as np

dx = 0.000001


def f(x):
    return 2*x**2 + 3*x - 2


def tangent(func, x):
    return (func(x+dx)-func(x))/dx


def fd(x):
    return (f(x+dx)-f(x))/dx


X = np.linspace(-10, 10, 100)
plt.plot(X, f(X), label='f(x)')
plt.plot(X, fd(X), label='f\'(x)')
plt.legend()
plt.grid()
plt.show()
