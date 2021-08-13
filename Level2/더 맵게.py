import heapq
scoville = [1, 2, 3, 9, 10, 12]
k = 15

def solution(scoville, k):
    heapq.heapify(scoville) #리스트를 힙으로 만들어준다
    count = 0
    while scoville[0] < k:
        tmp = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, tmp) #섞은 걸 힙에 다시 넣어준다
        count += 1
        if len(scoville) == 1 and scoville[0] < k:
            return -1
    return count


did = solution(scoville, k)
print(did)