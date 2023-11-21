from heapq import *
from collections import defaultdict


def solution(n, costs):
    answer = 0
    dic = defaultdict(list)

    # 비용, 시작점, 도착점
    for item in costs:
        dic[item[0]].append((item[2], item[0], item[1]))
        dic[item[1]].append((item[2], item[1], item[0]))

    connected = {0}
    candidate = dic[0]
    heapify(candidate)

    while candidate:
        cost, start, end = heappop(candidate)
        if end not in connected:
            connected.add(end)
            answer += cost

            for k in dic[end]:
                if k[2] not in connected:
                    heappush(candidate, k)

    return answer


