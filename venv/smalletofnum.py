limit = int(input("enter a limit"))
print("enter",limit,"numbers")
small = int(input())
for count in range(limit-1):
  num = int(input())
  if small > num:
    small = num
print("smallest element is ",small)