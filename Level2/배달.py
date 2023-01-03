N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3


def solution(N, road, K):
    each = [0] * N
    total = [each] * N
    print(total)

    for i in range(len(road)):
        print(total[road[i][0] - 1][road[i][1] - 1])
        print(road[i][2])
        total[road[i][0] - 1][road[i][1] - 1] = road[i][2]
        print(total)

print(solution(N, road, K))

