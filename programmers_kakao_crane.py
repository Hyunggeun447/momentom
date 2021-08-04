def solution(board, moves):
    
    result=[]
    
    for i in moves:
        
        for j in range(0,len(board)):
            if board[j][i-1] ==0:
                pass
        
            elif board[j][i-1] !=0:
                result.append(board[j][i-1])
                board[j][i-1]=0
                break
        

    count=0
    y=1
    while y<len(result):
        if result[y-1]==result[y]:
            
            del result[y-1],result[y-1]
            count+=2
            y=1
        else:
            y+=1
        
    
    
    
    return count