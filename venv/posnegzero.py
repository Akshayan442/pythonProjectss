pos = 0
neg = 0
z = 0
num = int(input("enter a nos"))
for count in range(num):
  a = int(input("enter number"))
  if a > 0:
    pos = pos + 1
  elif a < 0:
    neg = neg + 1
  else:
    z = z + 1
print("number of positive nos ",pos)
print("number of negative nos ",neg)
print("number of zeros ",z)
