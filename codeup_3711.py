
import math

a,b,k=input().split()
a=int(a)
n=int(b)
k=int(k)


def how_many(a,n,k):
  arr=[0]*(n+10)
  arr[0]=0
  arr[k]=1

  if n>9:
    for i in range(10,n+1):
      x=math.floor(math.log10(i))
      if (i//(10**x))==k:
        arr[i]=1+arr[i%(10**x)]
      else:
        arr[i]=arr[i%10**x]
  
  total=[0]*(n+1)
  total[0]=0
  for i in range(a,n+1):
    total[i]=total[i-1]+arr[i]


  return total[n]



print(how_many(a,n,k))