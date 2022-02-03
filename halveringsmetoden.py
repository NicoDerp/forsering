x1 = -10
x2 = 10
n = 100

def f(x):
	return 3**x - x - 3

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

print(f"f(x) = 0\nx = ({midt_x, midt_y})")
