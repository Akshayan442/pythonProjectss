num = int(input("enter a number"))
fact = 1
if num < 0:
  print("not factorial")
elif num == 0:
  print("factorial")
else:
  for i in range(1,num + 1):
    fact = fact * 1
  print("factorial of ",num,"is",fact)