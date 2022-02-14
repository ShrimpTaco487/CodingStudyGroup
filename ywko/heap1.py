import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    heap_length = len(scoville)
    while scoville[0] < K:
        if answer is heap_length - 1:
            answer = -1
            break
        left_k = heapq.heappop(scoville)
        right_k = heapq.heappop(scoville)
        new_k = left_k + right_k*2
        heapq.heappush(scoville,new_k)
        heapq.heapify(scoville)
        answer += 1
    
    return answer
