def solution(n):
    arr=[]
    end=0
    for i in range(1,n+1):
        arr.append([0]*i)
        end+=i




    k=1


    for c in range(0,(n//3)+1):
        for i in range(0,n-3*c):
            arr[i+2*c][c]=k
            k+=1

        for i in range(0,n-2-3*c):
            arr[n-1-c][1+c+i]=k
            k+=1


        for i in range(0,n-3*c-1):
            arr[n-1-i-c][n-1-i-2*c]=k
            k+=1



    arr_total=[]
    for i in range(0,n):
        arr_total+=arr[i]
    
    if n==1:
        arr_total=[1]
        
    

    
    return arr_total