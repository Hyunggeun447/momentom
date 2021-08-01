n=int(input())

for j in range(0,n):
  for i in range(1,n+1):
    print(n*j+n-i+1,end=" ")
  print()