def solution(array, commands):
    answer = []
    
    for i in range(0,len(commands)):
        arr=array[(commands[i][0]-1):commands[i][1]]
        
    
        arr.sort()
        answer.append(arr[(commands[i][2]-1)])
    
    
    return answer