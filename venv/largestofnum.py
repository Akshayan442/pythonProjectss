limit = int(input("enter a limit"))
print("enter",limit,"numbers")
lar = int(input())
for count in range(limit-1):
  num = int(input())
  if lar < num:
    lar = num
print("largest element is ",lar)