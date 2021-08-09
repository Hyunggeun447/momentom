def solution(scores):
    answer = ''
    
    arr=[]
    
    for i in range(0,len(scores)):
        arr_sub=[]
        for j in range(0,len(scores)):
            arr_sub.append(scores[j][i])

        arr.append(arr_sub)



    x=[]

    for i in range(0,len(scores)):
        if (arr[i][i]==min(arr[i]) or arr[i][i]==max(arr[i])) and arr[i].count(arr[i][i])==1:
            x.append((sum(arr[i])-arr[i][i])/(len(arr)-1))
        else:
            x.append(sum(arr[i])/len(arr))

    print(x)

    for i in range(0,len(x)):
        if x[i]>=90:
            answer+="A"
        elif x[i]>=80:
            answer+="B"
        elif x[i]>=70:
            answer+="C"
        elif x[i]>=50:
            answer+="D"
        else:
            answer+="F"
    
               
        
    
    return answer