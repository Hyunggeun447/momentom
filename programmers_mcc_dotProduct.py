def solution(a, b):
    arr=[]
    for i in range(0,len(a)):
        arr.append(a[i]*b[i])
        
    answer=sum(arr)
    return answer