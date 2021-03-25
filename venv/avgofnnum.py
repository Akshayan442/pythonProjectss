n = int(input("how many numbers"))
sum = 0
for i in range(0,n):
  num = int(input("enter a number"))
  sum = sum + num
avg = sum / num
print("average of",n,"number is  ",avg)