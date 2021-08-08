def solution(numbers):
    answer = []
    
    arr=[]
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            arr.append(numbers[i]+numbers[j])
        
    answer=sorted(set(arr))
    return answer