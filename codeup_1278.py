n=int(input())
i=0
while True:
  k=n//(10**i)
  if k!=0:
    i=i+1
  else:
    print(i)
    break