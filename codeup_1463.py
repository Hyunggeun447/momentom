n=int(input())

for j in range(n,0,-1):
  for i in range(1,n+1):
    print(j+n*(i-1),end=" ")
  print()