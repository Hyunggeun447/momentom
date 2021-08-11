def solution(a):
    answer=3
    
    if len(a)>3:
        s=a[1:-1]
        k=a.index(min(s))
        x=a[0]

        for i in range(1,k):
            if a[i]<x:
                answer+=1
                x=a[i]
        
        y=a[-1]
        for i in range(len(a)-1,k,-1):
            if a[i]<y:
                answer+=1
                y=a[i]
    else:
        answer=len(a)
    
    
            
            

        
    
    return answer