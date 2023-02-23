# 유효한 좌표값인지 확인해주는 함수
def canGo(x, y, width, height):
    return x >= 0 and x < height and y < width and y >= 0


def solution(maps):
    # 움직임의 방향 세트
    dir_x = [-1, 1, 0, 0]
    dir_y = [0, 0, -1, 1]
    width = len(maps[0])
    height = len(maps)
    answer = []
    tmp = []

    # 거친곳인지 확인해주는 배열
    index = [[0] * width for i in range(height)]

    def DFS(x, y):
        # 1. 타당한 좌표값인지
        if canGo(x, y, width, height):
            # 2. 거치지 않았던 좌표
            if index[x][y] == 0:
                # 3.1 현 좌표가 바다가 아닐 경우
                if maps[x][y] != 'X':
                    # 4.1 현재 좌표에 적힌 숫자 저장
                    tmp.append(int(maps[x][y]))

                    # 5. 거쳤던 좌표임을 표시
                    index[x][y] = 1

                    # 6. 사방으로 연결된 숫자가 있는지 탐색 시작 (상하좌우)
                    DFS(x + dir_x[0], y + dir_y[0])
                    DFS(x + dir_x[1], y + dir_y[1])
                    DFS(x + dir_x[2], y + dir_y[2])
                    DFS(x + dir_x[3], y + dir_y[3])

                # 3.2 현 좌표가 바다인 경우
                else:
                    # 4.2 거쳐간 좌표임을 표시
                    index[x][y] = 1

    for i in range(0, height):
        for j in range(0, width):
            DFS(i, j)

            if len(tmp) > 0:
                answer.append(sum(tmp))
                tmp = []

    if len(answer) == 0:
        return [-1]
    else:
        answer.sort()
        return answer