def solution(answers):
    answer = []
    x=0
    y=0
    z=0
    l=len(answers)
    arr1=[1,2,3,4,5]*(l//5+1)
    arr2=[2,1,2,3,2,4,2,5]*(l//8+1)
    arr3=[3,3,1,1,2,2,4,4,5,5]*(l//10+1)
    for i in range(0,len(answers)):
        if answers[i]==arr1[i]:
            x+=1
        if answers[i]==arr2[i]:
            y+=1
        if answers[i]==arr3[i]:
            z+=1
            
    if x>=y and x>=z:
        answer.append(1)
    if y>=x and y>=z:
        answer.append(2)
    if z>=y and z>=x:
        answer.append(3)    
    
    return answer