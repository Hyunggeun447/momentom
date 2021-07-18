import math

n=int(input())
a = [int(x) for x in input().split()]
b,c=map(int, input().split())
s=0
for i in range(0,n):
  if a[i]>b:
    d=1+math.ceil((a[i]-b)/c)
    s=s+d
  else:
    s=s+1


print(s)