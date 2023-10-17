from collections import deque


# 해당 좌표가 영역 내의 타당 좌표인지 판단
def isOk(size, a, b):
    return 0 <= a < size and 0 <= b < size


# 최초 지뢰 좌표 찾기
def find_first(size, matrix):
    mines = []
    for a in range(size):
        if 1 in matrix[a]:
            for b in range(size):
                if matrix[a][b] == 1:
                    mines.append((a, b))
    return mines


def solution(board):
    answer = 0
    size = len(board)

    # 좌표 탐색 여부 기록 리스트
    index = [[0] * size for _ in range(size)]
    # 위험지역 수
    count = 0

    start = find_first(size, board)

    if len(start) == 0:
        return size ** 2
    else:
        dir_x = [0, 0, 1, 1, 1, -1, -1, -1]
        dir_y = [1, -1, 0, -1, 1, -1, 1, 0]

        for idx in range(len(start)):
            _x = start[idx][0]
            _y = start[idx][1]
            index[_x][_y] = 1

            for cnt in range(8):
                dx = _x + dir_x[cnt]
                dy = _y + dir_y[cnt]

                if isOk(size, dx, dy) == False:
                    continue

                if index[dx][dy] == 1:
                    continue

                if board[dx][dy] == 0:
                    index[dx][dy] = 1
                    count += 1
                    continue

        return (size ** 2) - len(start) - count
