

a,b,k=input().split()
a=int(a)
b=int(b)
k=str(k)

s=[0]

for i in range(a,b+1):
  s.append(str(i).count(k))


print(sum(s))