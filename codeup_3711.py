import math

n=int(input())
k=int(input())


def how_many(n,k):
  arr=[0]*(n+1)
  arr[0]=0
  arr[k]=1

  if n>9:
    for i in range(10,n+1):
      x=math.floor(math.log10(i))
      if (i//(10**x))==k:
        arr[i]=1+arr[i%(10**x)]
      else:
        arr[i]=arr[i%10**x]

  return arr[n]

print(how_many(n,k))