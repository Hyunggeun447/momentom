def solution(a, b):
    if a>b:
        a,b=b,a
    
    x=0
    for i in range(a,b+1):
        x+=i
    return x