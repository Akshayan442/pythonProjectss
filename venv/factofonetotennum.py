i = 1
fact = 1
j = 1
while i <= 10:
    while j <= i:
        fact = fact * j
        j = j + 1
    print("factorial of",i,"is",fact)
    i = i + 1