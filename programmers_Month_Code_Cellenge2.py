
def solution(left, right):
    
    arr=[]
    for j in range(left,right+1):
        arr_sub=[]
        if j>1:
            for i in range(1,(j//2)+1):
                if j%i==0:
                    arr_sub.append(i)
                    arr_sub.append(j//i)
        elif j==1:
            arr_sub=[1]
        arr.append(set(arr_sub))
            
    print(arr)       
    x=0
    for i in range(0,len(arr)):
        if len(arr[i])%2==0:
            x+=max(arr[i])
        else:
            x-=max(arr[i])
    
    
    return x