a,b=map(int, input().split())
x=0
while True:
    if a==b:
        print(x)
        break
    elif a+10<b:
        a=a+10
        x+=1
    elif a+5<b:
        a=a+5
        x+=1
    elif a+1<b:
        a=a+1
        x+=1
    elif a>b+1:
        a=a-1
        x+=1
    elif a>b+5:
        a=a-5
        x+=1
    elif a>b+10:
        a=a-10
        x+=1