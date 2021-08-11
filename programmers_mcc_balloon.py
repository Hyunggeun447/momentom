def solution(a):
    answer = 2
    if len(a)<=3:
        answer=len(a)
    
    else:
        for i in range(1,len(a)-1):


            min1=min(a[:i])

            min2=min(a[i+1:])

            if a[i]>min1 and a[i]>min2:
                continue
            else:
                answer+=1
        
    
    return answer