import numpy as np
import matplotlib.pyplot as plt

nøyaktighet = 100
def_verdier = [-5, 10]

X = np.linspace(def_verdier[0], def_verdier[1], nøyaktighet)

def f(x):
	return 2**x - 5*x

def g(x):
	return 2**x + 3**(-x) - 3


f_Y = f(X)
g_Y = g(X)

nullpunkt = []
for i in range(nøyaktighet):
	# print("f({}) = {}".format(X[i], f_Y[i]))
	# print("g({}) = {}\n".format(X[i], g_Y[i]))

	# print("f({}) - g({}) = {}".format(X[i], X[i], diff))

	diff = f_Y[i] - g_Y[i]
	if -1 < diff < 1: # Endre for mer nøyaktighet
		x = round(X[i], 4)
		y = round(f_Y[i], 4)
		print("Nullpunkt på ({}, {})".format(x, y))


plt.plot(X, f_Y)
plt.plot(X, g_Y)
plt.grid()
plt.show()



