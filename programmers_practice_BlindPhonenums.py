def solution(phone_number):
    answer = ''
    l=len(phone_number)
    
    answer='*'*(l-4)+phone_number[-4:]
    return answer