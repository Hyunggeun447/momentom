def solution(n):
    arr=[]

    for i in range(1,n+1):
         arr.append([0]*i)


    end=0
    for i in range(1,n+1):
         end+=i

    k=1
    c=0


    while True:
        
        for i in range(1+c*2,n+1-2*c):
                arr[i-1][c]=k
                k+=1
            
        for i in range(1,n-2*c):
                arr[n-c-1][i]=k
                k+=1

        j=0
        if n-2-c>2*c:
            for i in range(n-2-c,0+2*c,-1):
                arr[i][n-2-2*c-j]=k
                k+=1
                j+=1
        c+=1
        if k==end+1:
            break

    arr_total=[]

    for i in range(0,n):
         arr_total+=arr[i]

    
    return arr_total