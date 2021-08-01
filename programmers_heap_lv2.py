import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        
        if len(scoville)<2 and scoville[0]<K:
            answer=-1
            break
            
        x=heapq.heappop(scoville)
        y=heapq.heappop(scoville)
        heapq.heappush(scoville, x+2*y)
        answer+=1
        if scoville[0]>=K:
            break
    
      


    return answer