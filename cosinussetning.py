from math import degrees, acos

a = float(input("Skriv inn side a: "))
b = float(input("Skriv inn side b: "))
c = float(input("Skriv inn side c: "))

A_rad = acos((a**2 - b**2 - c**2) / (-2*b*c))
B_rad = acos((b**2 - a**2 - c**2) / (-2*a*c))
C_rad = acos((c**2 - a**2 - b**2) / (-2*a*b))

A = degrees(A_rad)
B = degrees(B_rad)
C = degrees(C_rad)

print(f"A = {A:.2f}")
print(f"B = {B:.2f}")
print(f"C = {C:.2f}")
