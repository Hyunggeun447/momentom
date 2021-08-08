def solution(dartResult):
    answer = 0
    arr=[]
    arr1=[]
    arr2=[]
    arr3=[]
    nums=['0','1','2','3','4','5','6','7','8','9','10']
    for i in dartResult:
         arr.append((i))
        
    print(arr)


    arr1.append(arr[0])
    del arr[0]
    
    while True:
        arr1.append(arr[0])
        del arr[0]
        if arr[0] in nums:
            break


    arr2.append(arr[0])
    del arr[0]
    
    while True:
        arr2.append(arr[0])
        del arr[0]
        if arr[0] in nums:
            break

    arr3.append(arr[0])
    del arr[0]
    
    while True:
        arr3.append(arr[0])
        del arr[0]
        if len(arr)==0:
            break
            
    if arr1[0]=='1' and arr1[1]=='0':
        arr1[0]='10'
        del arr1[1]
    if arr2[0]=='1' and arr2[1]=='0':
        arr2[0]='10'
        del arr2[1]
    if arr3[0]=='1' and arr3[1]=='0':
        arr3[0]='10'
        del arr3[1]
    

    print(arr1)
    print(arr2)
    print(arr3)

    x=int(arr1[0])
    y=int(arr2[0])
    z=int(arr3[0])

    if arr1[1]=='S':
         x=x
    elif arr1[1]=='D':
          x=x**2
    elif arr1[1]=='T':
         x=x**3

    if arr2[1]=='S':
          y=y
    elif arr2[1]=='D':
          y=y**2
    elif arr2[1]=='T':
          y=y**3

    if arr3[1]=='S':
          z=z
    elif arr3[1]=='D':
          z=z**2
    elif arr3[1]=='T':
          z=z**3


    if len(arr1)==3:
        if arr1[2]=='*':
            x=2*x
        elif arr1[2]=='#':
            x=-1*x

    if len(arr2)==3:
        if arr2[2]=='*':
            x=2*x
            y=2*y
        elif arr2[2]=='#':
            
            y=-1*y


    if len(arr3)==3:
        if arr3[2]=='*':
            y=2*y
            z=2*z
        elif arr3[2]=='#':
                 
            z=-1*z
    
    k=x+y+z


    


    return k