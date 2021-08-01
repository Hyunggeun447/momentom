n=int(input())

for j in range(1,n+1):
  for i in range(0,n):
    if j%2==0:
      print((j-1)*n+1+i,end=" ")
    else:
      print(n*j-i, end=" ")
  print()
