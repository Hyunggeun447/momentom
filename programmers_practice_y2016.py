def solution(a, b):
    answer = ''
    month=[0,31,29,31,30,31,30,31,31,30,31,30]
    day=["THU","FRI","SAT","SUN","MON","TUE","WED"]
    k=(sum(month[:a])+b)%7
    answer=day[k]
    
    
    
    return answer