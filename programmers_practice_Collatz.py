def solution(num):
    
    
    x=0
    
    while True:
        if num==1:
            break
        elif num%2==0:
            num=num/2
            x+=1
        elif num%2==1:
            num=3*num+1
            x+=1
        
        if x==501:
            x=-1
            break
            
    
    return x