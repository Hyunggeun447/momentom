n = int(input())      
a = input().split()

for i in range(n):
  a[i]=int(a[i])

min_num=a[0]

for i in range(n):
  if min_num > a[i]:
    min_num=a[i]
 
print(min_num)