print("enter the 3 coefficients")
a = int(input())
b = int(input())
c = int(input())
if a == 0:
  print("not quadratic eqn")
else:
  d = b*b - 4*a*c
  if d < 0:
    print("imaginary roots")
  elif d == 0:
    root = -b / (2 * a)
  else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("root1 s ",root1)
    print("root2 s ",root2)