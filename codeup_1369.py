n,m=map(int, input().split())
if n>=m:
  k= (n//m)*(m+1)
  print(k)

  print("*"*n)
  arr=[0]*(k)
  for i in range(0,k):
      if (i+3)%m==0:
        arr[i]='*'


  for i in range(0,n-2):
    print('*',end="")
      
    for x in range(0,n-2):
      print(str(arr[x]).replace("0"," "),end="")
      
    print('*')
    arr.append(arr[0])
    del arr[0]

    

    
  if n>1:
    print("*"*n)

else:
  print('*'*n)
  for i in range(0,n-2):
    print('*',end="")
    print(' '*(n-2),end="")
    print('*')
  print('*'*n)