n1 = float(input("enter first number"))
n2 = float(input("enter second number"))
n3 = float(input("enter third number"))
if(n1 > n2) and (n1 > n3):
  lar = n1
elif(n2 > n1) and (n2 > n3):
  lar = n2
else:
  lar = n3
print("largest number ",lar)