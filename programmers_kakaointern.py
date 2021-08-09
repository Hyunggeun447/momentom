


def solution(numbers, hand):
    answer = ''
    def distance(a,b):
        
        return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    
    r=[4,3]
    l=[4,1]
    
    for i in numbers:
        if i ==1 or i==4 or i==7:
            answer+='L'
            if i==1:
                l=[1,1]
            elif i==4:
                l=[2,1]
            elif i==7:
                l=[3,1]
        elif i==3 or i== 6 or i==9:
            answer+='R'
            if i==3:
                r=[1,3]
            elif i==6:
                r=[2,3]
            elif i==9:
                r=[3,3]
        
        elif i==2 or i==5 or i==8 or i==0:
            if i==2:
                k=[1,2]
                if distance(r,k)<distance(l,k):
                    answer+='R'
                    r=k
                elif distance(r,k)>distance(l,k):
                    answer+='L'
                    l=k
                elif distance(r,k)==distance(l,k):
                    if hand=="right":
                        answer+='R'
                        r=k
                    else:
                        answer+='L'
                        l=k
            elif i==5:
                k=[2,2]
                if distance(r,k)<distance(l,k):
                    answer+='R'
                    r=k
                elif distance(r,k)>distance(l,k):
                    answer+='L'
                    l=k
                elif distance(r,k)==distance(l,k):
                    if hand=="right":
                        answer+='R'
                        r=k
                    else:
                        answer+='L'
                        l=k
            elif i==8:
                k=[3,2]
                if distance(r,k)<distance(l,k):
                    answer+='R'
                    r=k
                elif distance(r,k)>distance(l,k):
                    answer+='L'
                    l=k
                elif distance(r,k)==distance(l,k):
                    if hand=="right":
                        answer+='R'
                        r=k
                    else:
                        answer+='L'
                        l=k
        
            elif i==0:
                k=[4,2]
                if distance(r,k)<distance(l,k):
                    answer+='R'
                    r=k
                elif distance(r,k)>distance(l,k):
                    answer+='L'
                    l=k
                elif distance(r,k)==distance(l,k):
                    if hand=="right":
                        answer+='R'
                        r=k
                    else:
                        answer+='L'
                        l=k
                        
                        
            
    
    return answer