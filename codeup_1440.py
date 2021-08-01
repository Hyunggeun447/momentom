n=int(input())
arr=input().split()
for i in range (0,n):
  arr[i]=int(arr[i])

for j in range(0,n):
  print("{}:".format(j+1),end=" ")
  for i in range(0,n):
    if i == j:
      pass
    elif arr[j]<arr[i]:
      print("<",end=" ")
    elif arr[j]>arr[i]:
      print(">",end=" ")
    elif arr[j]==arr[i]:
      print("=",end=" ")
  print()