a,b=map(int, input().split())
if a>b:
  a,b=b,a


k=b-a

x=0
x=k//10
k= k%10
if 3<k<10:
  if k>7:
    k=k-10
    x+=1+abs(k)
  else:
    k=k-5
    x+=1+abs(k)
else:
  x=k+x

print(x)