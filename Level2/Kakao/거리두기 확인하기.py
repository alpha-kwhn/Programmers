places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = [0, 0, 0, 0, 0]


def BFS(graph, a, b):
    queue = deque([(a, b)])
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
            continue

        if graph[nx][ny] == "P":
            return False

        elif graph[nx][ny] == "X":
            continue

        else:
            if graph[nx][ny] == "O":
                count = 0
                for j in range(4):
                    if count == 1:
                        return False
                    else:
                        px = nx + dx[j]
                        py = ny + dy[j]
                        if px < 0 or py < 0 or px >= 5 or py >= 5:
                            continue
                        if px == x and py == y:
                            continue
                        if graph[px][py] == "P":
                            count += 1
                        else:
                            continue
    return True


def solution(places):
    for i in range(5):
        tmp = ''.join(places[i])
        if "P" not in tmp:
            result[i] = 1
        else:
            check = []
            for j in range(5):
                for p in range(5):
                    if places[i][j][p] == "P":
                        check.append(BFS(places[i], j, p))
            if False not in check:
                result[i] = 1
    return result


print(solution(places2))






