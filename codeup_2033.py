k,n=map(int, input().split())
line=[]

for i in range (0,k+1):
  line.insert(i,i)


while n>0:
  a,b=map(int, input().split())
  c=line.index(a)
  d=line.index(b)
  line[c],line[d]=line[d],line[c]


  n=n-1


s=int(input())

print(line[s]) 