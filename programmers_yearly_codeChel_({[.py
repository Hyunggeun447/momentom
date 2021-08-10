def solution(s):
    
    count=0
    
    for i in range(0,len(s)):
        a=s
        while True:
            if "{}" in a:
                a=a.replace("{}","")
            elif "[]" in a:
                a=a.replace("[]","")
            elif "()" in a:
                a=a.replace("()","")
            else:
                break
        if len(a)==0:
            count+=1
        s=s[1:]+s[0]
    
    print(count)
    
    
    return count