def solution(s):
    answer = ''
    arr=[]
    for i in s:
        arr.append(i)
    l=len(s)
    if l%2==1:
        answer=s[(l)//2]
    else:
        answer=s[l//2-1:l//2+1]
    return answer