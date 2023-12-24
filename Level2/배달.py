def solution(N, road, K):
    vilage = [[1e8] * N for _ in range(N)]
    answer = 1

    for idx in road:
        if vilage[idx[0] - 1][idx[1] - 1] == 0 and vilage[idx[1] - 1][idx[0] - 1] == 0:
            vilage[idx[0] - 1][idx[1] - 1] = idx[2]
            vilage[idx[1] - 1][idx[0] - 1] = idx[2]
        elif vilage[idx[0] - 1][idx[1] - 1] > 0 and vilage[idx[1] - 1][idx[0] - 1] > 0:
            vilage[idx[0] - 1][idx[1] - 1] = min(vilage[idx[0] - 1][idx[1] - 1], idx[2])
            vilage[idx[1] - 1][idx[0] - 1] = min(vilage[idx[0] - 1][idx[1] - 1], idx[2])

    for path in range(N):
        for start in range(N):
            for end in range(N):
                vilage[start][end] = min(vilage[start][end], vilage[start][path] + vilage[path][end])

    for idx in range(1, len(vilage[0])):
        if 0 < vilage[0][idx] <= K:
            answer += 1

    return answer