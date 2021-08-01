n,m=map(int, input().split())

for j in range(n,0,-1):
  for i in range(0,m):
    print(j*m-i,end=" ")
  print()
