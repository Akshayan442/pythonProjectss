l1 = [10,20,30,40,50]
l2 = [60,25,30,10]
print(len(l1))
print(len(l2))
total = sum(l1)
print("sum of list1",total)
total = sum(l2)
print("sum of list2",total)
l3 = []
for n in l1:
    if n in l2:
        if n not in l3:
            l3.append(n)
print(l3)
