def solution(s):
    answer = ''
    
    split=s.split(" ")
    print(split)
    for i in range(0,len(split)):
        for j in range(0,len(split[i])):
            
            if j%2!=0:
                answer+=split[i][j].lower()
            else:
                answer+=split[i][j].upper()
        if i<len(split)-1:
            answer+=" "
    
    
    
    
    
    return answer