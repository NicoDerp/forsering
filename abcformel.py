from math import sqrt

a, b, c = [float(i) for i in input("Skriv a, b, c: ").split(', ')]

n = b*b - 4*a*c
if n < 0:
    print("Ingen reele løsninger!")
elif n == 0:
    # En løsning
    x = -b / (2*a)
    print("x =", x)
else:
    n = sqrt(n)
    x1 = (-b+n)/(2*a)
    x2 = (-b-n)/(2*a)
    print("x = {}  V  {}".format(x1, x2))
