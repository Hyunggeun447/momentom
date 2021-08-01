n,m=map(int, input().split())

for j in range(0,n):
  for i in range(0,m):
    print((m*n-j)-i*n,end=" ")
  print()
