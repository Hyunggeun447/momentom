k,n=map(int, input().split())

total=k//n
a=k//n
b=k%n
c=a+b
 
while c >= n:
  total=total + c//n
  a=c//n
  b=c%n
  c=a+b
  
  

print(total)