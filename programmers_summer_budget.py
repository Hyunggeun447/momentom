def solution(d, budget):
    answer = 0
    
    d.sort()
    
    k=0
    i=0
    if len(d)>1:
        while True:
            k+=d[i]
            i+=1
            if k==budget:
                answer=i
                break
            elif k>budget:
                answer=i-1
                break
            elif i==len(d):
                answer=i
                break
    elif len(d)==1:
        if d[0]<=budget:
            answer=1
        else:
            answer=0
    return answer