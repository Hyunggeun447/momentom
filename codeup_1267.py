n=int(input())
nums=input().split()
for i in range(len(nums)):
    nums[i]=int(nums[i])
    
x=0
for i in range(0,n):
    if nums[i]%5==0:
        x+=nums[i]
        
print(x)