num1 = int(input("enter the first num"))
num2 = int(input("enter the second num"))
num3 = int(input("enter the third num"))
if(num1 < num2)and(num1 < num3):
    small = num1
elif(num2 < num1)and(num2 < num3):
    small = num2
else:
    small = num3
print("smmallest number",small)
