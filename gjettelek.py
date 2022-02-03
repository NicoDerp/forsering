from random import randint

a = 0
b = 100

riktig = randint(a, b)

print(f"Det riktige er {riktig}")

gjett = 0
while 1:
	n = int((a+b)/2)

	print(f"Gjetter {n}...")

	# Riktig
	if n == riktig:
		break

	# For høyt
	if n > riktig:
		b = n

	# For lavt
	if n < riktig:
		a = n

	gjett += 1

print(f"Fant et svar på {gjett} gjett. Svaret var {riktig}")
