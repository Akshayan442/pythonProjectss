import math
print("Enter the 3 co-efficient")
a = int(input())
b = int(input())
c = int(input())
if a == 0:
    print("Not Quadratic equation")
else:
    d = b*b - 4*a*c
    if d < 0:
        print("Imaginary roots")
    elif d == 0:
        root = -b / (2 *a)
        print("roots are:", root, root)
    else:
        root1 = (-b + math.sqrt(d))/(2 * a)
        root2 = (-b - math.sqrt(d))/(2 * a)
        print("root1 is:", root1)
        print("root2 is:", root2)
