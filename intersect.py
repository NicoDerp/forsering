def f(x):
  return 0.5 * x**2 + 2*x + 1

def g(x):
  return x**3 + 2

x = -100
d = 0.0001

while (abs(f(x) - g(x)) > 1):
  x += d

print(f"({x:0.5f}, {f(x):0.5f})")
