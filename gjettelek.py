from random import randint

antall = 1000
sum = 0

for _ in range(antall):
	a = 0
	b = 100

	riktig = randint(a, b)
	print(f"Det riktige er {riktig}")
	gjett = 0
	while 1:
		n = int(round((a+b)/2, 0))

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

	gjett += 1
	sum += gjett
	print(f"Fant et svar på {gjett} gjett. Svaret var {riktig}")

relativ_frekvens = sum / antall
print(f"Gjorde {antall} gjett med sum {sum}.\nRelativ frekvens er {relativ_frekvens}")
