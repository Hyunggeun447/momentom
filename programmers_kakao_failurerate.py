def solution(n, stages):
    answer = []
    
    l=len(stages)

    dic={}
    for i in range(1,n+2):
        dic[i]=0

    for i in stages:
        dic[i]+=1

    dic_total={0:0}
    for i in range(1,n+2):
        dic_total[i]=dic_total[i-1]+dic[i]

    dic_percent={}

    for i in range(1,n+2):
        if (l-dic_total[i-1]) !=0:
            dic_percent[i]=dic[i]/(l-dic_total[i-1])
        else:
            dic_percent[i]=dic[i]/(l+1-dic_total[i-1])

    del dic_percent[n+1]


    dic_percent=sorted(dic_percent.items(), key=lambda x: x[1],reverse=True)



    for i in range(0,n):
        answer.append(dic_percent[i][0])
    
    
    
                 
    
    
    
    return answer