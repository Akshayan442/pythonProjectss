n = int(input("how many terms"))
n1, n2 = 0, 1
count = 0
if n <= 0:
  print("please enter positive integer ")
elif n == 1:
  print("fibinocci sequence upto",n)
  print(n1)
else:
  print("fib sequence")
  while count < n:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1