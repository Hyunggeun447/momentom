def solution(price, money, count):
    answer = -1
    
    x=[0]*(count+1)
    x[1]=price
    if count>=2:
        for i in range(2,count+1):
            x[i]=x[i-1]+i*price
    
    answer=x[-1]-money
    if answer<0:
        answer=0

    return answer