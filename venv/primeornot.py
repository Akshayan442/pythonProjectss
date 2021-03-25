num = int(input("enter a numer"))
i = 2
flag = 1
while i <= (num / 2):
  if num % i == 0:
    flag = 0
  i = i + 1
if flag == 1:
  print(" prime number")
else:
  print("not prime number")