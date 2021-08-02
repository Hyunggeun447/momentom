def solution(phone_book):
    answer = True
    phone_book.sort()

    for j in range(0,len(phone_book)):
        for i in range(j+1,len(phone_book)):
            if phone_book[j]==phone_book[i][:len(phone_book)]:
                
                answer=False
                break
    return answer