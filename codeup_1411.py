
n=int(input())

nums = [int(input()) for _ in range(n-1)]

totalsum= (n+1)*n/2

sum=sum(nums)



a=int(totalsum - sum)

print(a)