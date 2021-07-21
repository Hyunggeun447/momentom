
n=int(input())
arr=input().split()
for i in range(len(arr)):
    arr[i]=int(arr[i])


def atob_add(a,b,c):  #c(array) 의 a~b까지의 합
  t=0
  for i in range(a,b+1):
    t=t+c[i]
  return t

if n>=2 :
  max_value=0
  for y in range(n-1,-1,-1):
    for x in range(0,n):
      if arr[x]>0 and arr[y-1]>0:
        if max_value<atob_add(x,y,arr):
          max_value=atob_add(x,y,arr)
        elif x>y:
          break

elif n==1:
   max_value=arr[0]   

print(max_value)