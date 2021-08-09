

'''
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


    '''
    


def solution(numbers, hand):
    answer = ''
    
    left=[1,4,7]
    right=[3,6,9]
    middle=[0,2,5,8]
    l=10
    r=11
    
    for i in numbers:
        if i in left:
            answer+='L'
            l=i
        elif i in right:
            answer+='R'
            r=i
        elif i in middle:
            if i==2:
                k=[3,1,0,1,2,1,2,3,2,3,4,4]
                if k[l]<k[r]:
                    answer+="L"
                    l=i
                elif k[l]>k[r]:
                    answer+="R"
                    r=i
                elif k[l]==k[r]:
                    if hand=="right":
                        answer+="R"
                        r=i
                    else:
                        answer+="L"
                        l=i
                        
            elif i==5:
                k=[2,2,1,2,1,0,1,2,1,2,3,3]
                if k[l]<k[r]:
                    answer+="L"
                    l=i
                elif k[l]>k[r]:
                    answer+="R"
                    r=i
                elif k[l]==k[r]:
                    if hand=="right":
                        answer+="R"
                        r=i
                    else:
                        answer+="L"
                        l=i
                        
            elif i==8:
                k=[1,3,2,3,2,1,2,1,0,1,2,2]
                if k[l]<k[r]:
                    answer+="L"
                    l=i
                elif k[l]>k[r]:
                    answer+="R"
                    r=i
                elif k[l]==k[r]:
                    if hand=="right":
                        answer+="R"
                        r=i
                    else:
                        answer+="L"
                        l=i
                
            elif i==0:
                k=[0,4,3,4,3,2,3,2,1,2,1,1]
                if k[l]<k[r]:
                    answer+="L"
                    l=i
                elif k[l]>k[r]:
                    answer+="R"
                    r=i
                elif k[l]==k[r]:
                    if hand=="right":
                        answer+="R"
                        r=i
                    else:
                        answer+="L"
                        l=i
                    
            

                        
                        
            
    
    return answer