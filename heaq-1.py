from queue import PriorityQueue
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)   # Using heapify, heapq is generated from list.
    answer = 0
    while 1:
        if scoville[0] > K:   # heap[0] returns the smallest element. notice! heap[1] doesn't return smallest element.
            break
        if len(scoville) is 1:
            return -1
        A = heapq.heappop(scoville)    # pop
        B = heapq.heappop(scoville)
        new_K = A + B*2
        heapq.heappush(scoville, new_K) # push
        answer += 1

    return answer