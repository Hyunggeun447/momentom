
n=int(input())
arr=input().split()
for i in range(len(arr)):
    arr[i]=int(arr[i])


def fun(arr):
  t=[0]*len(arr)
  t[0]=arr[0]
  for i in range(0,len(arr)):
    t[i]=max(0,t[i-1])+arr[i]
  return max(t)


print(fun(arr))