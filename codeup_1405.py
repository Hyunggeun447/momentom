n=int(input())

arr=input().split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])

for i in range(0,n):
  print(arr[i], end=" ")
print()

for i in range (0,n-1):
    arr.append(arr[0])
    del arr[0]
    for i in range (0,n):
        print(arr[i],end=" ")
    print()