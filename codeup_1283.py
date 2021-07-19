a=int(input())
n=int(input())

b=input().split()


for i in range(n):
  b[i]=int(b[i])


t=a

for i in range(n):
  t=t*(100+b[i])/100

x=round(t-a)
print(x)
if x>0:
  print("good")
elif x==0:
  print("same")
else:
  print("bad")
