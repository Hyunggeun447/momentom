n=int(input())
arr=[
  [0]*n
  ]
for i in range(0,n):
  arr.append([0]*n)
for i in range(0,n):
  arr[0][i]=int(input())


for i in range(1,n):
  for j in range(0,n-1):
    arr[i][j]=arr[i-1][j+1]-arr[i-1][j]


'''
arr[0][0]
arr[0][1]  arr[1][0]
arr[0][2]  arr[1][1] arr[2][0]
arr[0][3]  arr[1][2] arr[2][1] arr[3]][0]
print(arr)
'''


for j in range(0,n):
  for i in range(0,j+1):
    print(arr[i][j-i],end=" ")
  print()
