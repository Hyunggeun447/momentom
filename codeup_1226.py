num1=input().split()
num2=input().split()
for i in range(0,len(num1)):
  num1[i]=int(num1[i])
for i in range(0,len(num2)):
  num2[i]=int(num2[i])

num3=num1[len(num1)-1]
del num1[len(num1)-1]


x=0
for i in range(0,len(num2)):
  if num2[i] in num1:
    x+=1

if x==6:
  print(1)
elif x==5:
  if num3 in num2:
    print(2)
  else:
    print(3)
elif x==4:
  print(4)
elif x==3:
  print(5)
else:
  print(0)