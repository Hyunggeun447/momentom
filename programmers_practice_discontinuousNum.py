def solution(arr):
    
    result=[]
    for i in range(0,len(arr)-1):
        if arr[i]!=arr[i+1]:
            result.append(arr[i])
    
    result.append(arr[-1])
        
    
    
    return result