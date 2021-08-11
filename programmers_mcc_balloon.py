def solution(a):
    answer=3
    
    if len(a)>3:
        s=a[1:-1]
        k=a.index(min(s))

        for i in range(1,k):
            if a[i]<a[0]:
                answer+=1
        

        for i in range(len(a)-1,k,-1):
            if a[i]<a[-1]:
                answer+=1
    else:
        answer=len(a)
    
    
            
            

        
    
    return answer