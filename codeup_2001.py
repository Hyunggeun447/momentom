#그리디

a=int(input())
b=int(input())
c=int(input())
x=a
if a>b:
  x=b
if b>c:
  x=c

d=int(input())
e=int(input())
y=d
if d>e:
  y=e

answer=float((x+y)*1.1)
print(format(answer,'.1f'))