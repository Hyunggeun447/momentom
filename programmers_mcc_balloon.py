def solution(a):
    answer = 1
      
    
    if len(a)>3:
        s=a[1:]
        k=a.index(min(s))
        if k==len(a)-1:
            for i in range(1,len(a)):
                if a[i]<a[0]:
                    answer+=1
        else:
            
            
            answer=answer+len(a)-k
            tem1=a[:k+1]
            
            for i in range(1,len(tem1)-1):
                if tem1[i]<tem1[0]:
                    answer+=1
            
        
            
    else:
        answer=len(a)
            
            
            

        
    
    return answer