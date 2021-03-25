num = int(input("enter number"))
ams = 0
a = num
while num > 0:
  d = num % 10
  ams = ams + (d * d * d)
  num = int(num / 10)
if ams == a:
  print(" an amstrong")
else:
  print(" not an amstrong")