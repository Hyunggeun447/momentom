def solution(n):
    
    arr=[]
    while True:
        n,a=divmod(n,3)
        arr.append(a)
        if n==0:
            break

    arr.reverse()
    print(arr)
    x=0

    for i in range(0,len(arr)):
        x+=arr[i]*(3**i)
    
        
    return x