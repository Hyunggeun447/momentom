def solution(nums):
    answer = 0
    l=len(nums)/2
    nums_set=list(set(nums))
    m=len(nums_set)
    
    if l<=m:
        answer=l
    else:
        answer=m
    return answer