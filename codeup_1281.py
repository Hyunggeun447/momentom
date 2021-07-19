a,b = map(int, input().split())

t=0
if a%2!=0:
    print(a,end="")
    t=a
else:
    print(-a,end="")
    t=-a

for i in range (a+1,b+1):
  if i%2==0:
    t=t-i
    print("-"+str(i),end="")
  else:
    t=t+i
    
    print("+"+str(i), end="")
  
  
print("="+str(t))