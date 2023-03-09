from collections import deque


# 해당 좌표가 타당한 좌표인지 검증
def isOK(x, y, width, height):
    return x >= 0 and x < height and y >= 0 and y < width


# 탐색 시작점 찾기
def start_point(maps):
    for i in range(len(maps)):
        if "S" not in maps[i]:
            continue
        else:
            return (i, maps[i].index("S"))


def solution(maps):
    dir_x = [1, -1, 0, 0]
    dir_y = [0, 0, 1, -1]
    width = len(maps[0])
    height = len(maps)
    index = [[0] * width for i in range(height)]

    lever_x = 0
    lever_y = 0
    lever_found = 0

    start = start_point(maps)
    queue = deque([[[start[0], start[1]]]])
    index[start[0]][start[1]] = 1

    count = 0

    while queue and lever_found == 0:
        container = []
        item = queue.popleft()

        for i in item:
            x = i[0]
            y = i[1]
            # 벽이 아닐때
            if maps[x][y] != "X":
                # 레버라면
                if maps[x][y] == "L":
                    lever_x = x
                    lever_y = y
                    lever_found = 1
                    container = []
                    break
                # 통로, 출구, 시작지점
                else:
                    # 탐색
                    if isOK(x + dir_x[0], y + dir_y[0], width, height) and index[x + dir_x[0]][y + dir_y[0]] == 0 and \
                            maps[x + dir_x[0]][y + dir_y[0]] != "X":
                        container.append([x + dir_x[0], y + dir_y[0]])
                        index[x + dir_x[0]][y + dir_y[0]] = 1
                    if isOK(x + dir_x[1], y + dir_y[1], width, height) and index[x + dir_x[1]][y + dir_y[1]] == 0 and \
                            maps[x + dir_x[1]][y + dir_y[1]] != "X":
                        container.append([x + dir_x[1], y + dir_y[1]])
                        index[x + dir_x[1]][y + dir_y[1]] = 1
                    if isOK(x + dir_x[2], y + dir_y[2], width, height) and index[x + dir_x[2]][y + dir_y[2]] == 0 and \
                            maps[x + dir_x[2]][y + dir_y[2]] != "X":
                        container.append([x + dir_x[2], y + dir_y[2]])
                        index[x + dir_x[2]][y + dir_y[2]] = 1
                    if isOK(x + dir_x[3], y + dir_y[3], width, height) and index[x + dir_x[3]][y + dir_y[3]] == 0 and \
                            maps[x + dir_x[3]][y + dir_y[3]] != "X":
                        container.append([x + dir_x[3], y + dir_y[3]])
                        index[x + dir_x[3]][y + dir_y[3]] = 1

        if len(container) != 0:
            count += 1
            queue.append(container)

    if lever_found == 0:
        return -1
    else:
        index = [[0] * width for i in range(height)]
        index[lever_x][lever_y] = 1
        queue = deque([[[lever_x, lever_y]]])

        while queue:
            container = []
            item = queue.popleft()

            for i in item:
                x = i[0]
                y = i[1]
                # 벽이아니라면
                if maps[x][y] != "X":
                    # 출구라면 카운트 리턴
                    if maps[x][y] == "E":
                        return count
                    else:
                        if isOK(x + dir_x[0], y + dir_y[0], width, height) and index[x + dir_x[0]][
                            y + dir_y[0]] == 0 and maps[x + dir_x[0]][y + dir_y[0]] != "X":
                            container.append([x + dir_x[0], y + dir_y[0]])
                            index[x + dir_x[0]][y + dir_y[0]] = 1
                        if isOK(x + dir_x[1], y + dir_y[1], width, height) and index[x + dir_x[1]][
                            y + dir_y[1]] == 0 and maps[x + dir_x[1]][y + dir_y[1]] != "X":
                            container.append([x + dir_x[1], y + dir_y[1]])
                            index[x + dir_x[1]][y + dir_y[1]] = 1
                        if isOK(x + dir_x[2], y + dir_y[2], width, height) and index[x + dir_x[2]][
                            y + dir_y[2]] == 0 and maps[x + dir_x[2]][y + dir_y[2]] != "X":
                            container.append([x + dir_x[2], y + dir_y[2]])
                            index[x + dir_x[2]][y + dir_y[2]] = 1
                        if isOK(x + dir_x[3], y + dir_y[3], width, height) and index[x + dir_x[3]][
                            y + dir_y[3]] == 0 and maps[x + dir_x[3]][y + dir_y[3]] != "X":
                            container.append([x + dir_x[3], y + dir_y[3]])
                            index[x + dir_x[3]][y + dir_y[3]] = 1

            if len(container) != 0:
                count += 1
                queue.append(container)

        return -1