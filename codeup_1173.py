h,m=input().split()

h=int(h)
m=int(m)

m=m-30

if m<0:
    m=m+60
    h=h-1
    if h<0:
        h=h+24
    
print(h,m)