list = [1,5,6,4,9,-6,8,2]
newlist = [x for x in list if x > 0]
print(newlist)

n = int(input("enter numbers"))
list = []
for x in range(n):
  x = int(input("enter no"))
  list.append(x)
print(list)
sqrlist = [x**2 for x in list]
print(sqrlist)

word = "umberella"
vowels = "aeiou"
list = [x for x in word if x in vowels]
print(list)

word = "flower"
list = []
for x in word:
  list.append(x)
  w = ord(x)
print(w)