from math import sqrt

org = 2

a = 0
b = org
n = 100

while n > 0:
  midt = (a+b)/2
  if midt**2 < org:
    a = midt
  else:
    b = midt
  n -= 1

print(f"sqrt(2) = {midt:0.4f}")
print(f"sqrt(2)**2 = {(midt**2):0.4f}")
print(f"a-sqrt(2) = {(midt-sqrt(2)):0.4f}")
