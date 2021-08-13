def solution(nums):
    nums.sort()
    
    tem=[]
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                tem.append(nums[i]+nums[j]+nums[k])
    
    x=max(tem)
    
    
    
    arr=set(range(2,x+1))
    
    for i in range(2,x+1):
        if i in arr:
            arr-=set(range(2*i,x+1,i))
    
    count=0
    for i in tem:
        if i in arr:
            count+=1
    

    
    return count