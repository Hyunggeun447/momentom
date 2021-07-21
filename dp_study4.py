
n=int(input())
arr=input().split()
for i in range(len(arr)):
    arr[i]=int(arr[i])



def max_sum(x,c):
  a=[0]
  for i in range (0,x):
    a.append(a[i]+c[i])
  return max(a)



def min_sum(x,c):
  a=[0]
  for i in range (0,x):
    a.append(a[i]+c[i])
  return min(a)

def index_max_sum(x,c):
  a=[0]
  for i in range (0,x):
    a.append(a[i]+c[i])
  a.reverse()
  return a.index(max(a))

k=n-index_max_sum(n,arr)

a=max_sum(n,arr)
b=min_sum(k,arr)


if n<2:
  print(arr[0])
else:
  if b<0:
    print(a-b)
  else:
    print(a)