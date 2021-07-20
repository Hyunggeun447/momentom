a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])

for i in range(len(a)):
  if (a[i]%5)==0:
    print(a[i])
    break
  elif(i==len(a)-1):
    print(0)