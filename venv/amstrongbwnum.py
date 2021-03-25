for i in range(100,1001):
  n = i
  ams = 0
  while n > 0:
    rem = n % 10
    ams = ams + (rem * rem * rem)
    n = int(n / 10)
  if ams == i:
    print(i)