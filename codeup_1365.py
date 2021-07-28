n=int(input())


print("*"*n)
arr=[0]*n

for i in range(0,n-2):
  print('*',end="")
  arr=[0]*(n-2)
  arr[i]="*"
  arr[n-3-i]='*'
  

  for i in range(0,n-2):
    print(str(arr[i]).replace("0"," "),end="")
  print('*')
print("*"*n)