from collections import deque


def isOK(a, b, width, height):
    return 0 <= a < height and 0 <= b < width


def DFS(a, b, direction, index, board):
    # 동, 서, 남, 북
    dir_x = [0, 0, 1, -1]
    dir_y = [1, -1, 0, 0]

    while True:
        nx = a + dir_x[direction]
        ny = b + dir_y[direction]

        if not isOK(nx, ny, len(board[0]), len(board)):
            return a, b, index

        if board[nx][ny] == "D":
            return a, b, index

        a = nx
        b = ny


def solution(board):
    answer = 0
    start_x = 0
    start_y = 0
    width = len(board[0])
    height = len(board)

    # 시작점 찾기
    for i in range(height):
        if "R" in board[i]:
            for j in range(width):
                if board[i][j] == "R":
                    start_x = i
                    start_y = j
                    break

    # BFS 탐색 시작
    queue = deque([[[start_x, start_y]]])
    # 동, 서, 남, 북
    dir_x = [0, 0, 1, -1]
    dir_y = [1, -1, 0, 0]
    index = [[0] * width for _ in range(height)]
    index[start_x][start_y] = 1

    while queue:
        target = queue.popleft()
        container = []

        for i in target:
            if board[i[0]][i[1]] == "G":
                return answer
            else:
                for j in range(4):
                    nx = i[0] + dir_x[j]
                    ny = i[1] + dir_y[j]

                    if not isOK(nx, ny, width, height):
                        continue

                    if board[nx][ny] == "D":
                        continue

                    nx, ny, index = DFS(nx, ny, j, index, board)

                    if index[nx][ny] == 0:
                        index[nx][ny] = 1
                        container.append([nx, ny])

        if len(container) > 0:
            answer += 1
            queue.append(container)

    return -1