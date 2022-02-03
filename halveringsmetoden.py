import matplotlib.pyplot as plt
import numpy as np

x1 = -100
x2 = 100
n = 100

def f(x):
	return 1.05 ** x - 12

while n != 0:
	y1 = f(x1)

	midt_x = (x1 + x2) / 2
	midt_y = f(midt_x)

	# Hvis de har forskjellige fortegn (pos * pos = pos, min * min = pos, pos * min = min)
	if midt_y * y1 < 0:  # For høyt
		x2 = midt_x

	else:  # For lavt
		x1 = midt_x

	n -= 1

print(f"f(x) = 0\nx = {midt_x:.4f}")

plot_width = 50
X = np.linspace(midt_x - plot_width/2, midt_x + plot_width/2, 100)
Y = f(X)

plt.plot(X, Y)
plt.grid()
plt.show()
