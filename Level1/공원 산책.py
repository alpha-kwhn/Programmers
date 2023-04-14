def isOK(a, b, width, height):
    return 0 <= a < width and 0 <= b < height


def solution(park, routes):
    dir_x = [1, -1, 0, 0]
    dir_y = [0, 0, 1, -1]
    start_x = 0
    start_y = 0
    width = len(park[0])
    height = len(park)
    nx = 0
    ny = 0

    for i in range(len(park)):
        if "S" in park[i]:
            start_x = i
            start_y = park[i].index("S")
            break

    for i in range(len(routes)):
        direction = routes[i][0]
        lengths = int(routes[i][2])
        flag = 0

        for j in range(lengths):
            if direction == "E":
                nx = start_x
                ny = start_y + (j + 1)
                if isOK(ny, nx, width, height) and park[nx][ny] != "X":
                    continue
                else:
                    flag = 1
                    break
            if direction == "W":
                nx = start_x
                ny = start_y - (j + 1)
                if isOK(ny, nx, width, height) and park[nx][ny] != "X":
                    continue
                else:
                    flag = 1
                    break
            if direction == "N":
                nx = start_x - (j + 1)
                ny = start_y
                if isOK(ny, nx, width, height) and park[nx][ny] != "X":
                    continue
                else:
                    flag = 1
                    break
            if direction == "S":
                nx = start_x + (j + 1)
                ny = start_y
                if isOK(ny, nx, width, height) and park[nx][ny] != "X":
                    continue
                else:
                    flag = 1
                    break
        if flag == 0:
            start_x = nx
            start_y = ny

    return [start_x, start_y]