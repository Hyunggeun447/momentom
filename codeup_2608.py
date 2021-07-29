n=int(input())
z=2**n -1

while True:
  a=format(z,'b')
  b=str(a)
  c=b.zfill(n)
  d=c.replace('0',"X",n)
  e=d.replace('1','O',n)
  print(e)
  z=z-1
  if z<0:
    break