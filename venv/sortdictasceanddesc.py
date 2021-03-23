dict1 = {}
print(type(dict1))
limit = int(input("Enter  the limit"))
for i in range(limit) :
    dict1.update({input("Enter the key") : input("Enter the value")})

l = list(dict1.items())
l.sort()
print("\n Ascending order is", l)

l = list(dict1.items())
l.sort(reverse=True)
print("\nDescending order is", l)

dict  = dict(l)

print("\nDictionary", dict)
print(("dict is" , dict1))