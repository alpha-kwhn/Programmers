maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

def solution(maps):
    def left(y, x):
        available = [0, 1, 2, 3, 4]  # 가능한 좌표값
        flag = 0
        lis = [y, x]
        for i in lis:
            if i not in available:
                flag = 1
        if flag == 0 and maps[y][x] == 1:
            return True

    def right(y, x):
        available = [0, 1, 2, 3, 4]  # 가능한 좌표값
        flag = 0
        lis = [y, x]
        for i in lis:
            if i not in available:
                flag = 1
        if flag == 0 and maps[y][x] == 1:
            return True

    def up(y, x):
        available = [0, 1, 2, 3, 4]  # 가능한 좌표값
        flag = 0
        lis = [y, x]
        for i in lis:
            if i not in available:
                flag = 1
        if flag == 0 and maps[y][x] == 1:
            return True

    def down(y, x):
        available = [0, 1, 2, 3, 4]  # 가능한 좌표값
        flag = 0
        lis = [y, x]
        for i in lis:
            if i not in available:
                flag = 1
        if flag == 0 and maps[y][x] == 1:
            return True
    result = []
    sample = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    def BFS(y, x, cost):
        lis = [right(y, x + 1), left(y, x - 1), up(y - 1, x), down(y + 1, x)]

        #print(y, x, cost)

        if True not in lis:
            result.append(-1)

        elif maps[3][4] == 0 and maps[4][3] == 0:
            result.append(-1)

        elif y == 4 and x == 4:
            return 0

        else:
            # 동 서 남 북
            if right(y, x + 1) == True:
                cost += 1
                result.append(cost)
                sample[y][x + 1] = 1
                BFS(y, x + 1, cost)
            else:
                if down(y + 1, x) == True:
                    cost += 1
                    result.append(cost)
                    sample[y + 1][x] = 1
                    BFS(y + 1, x, cost)
                else:
                    if up(y - 1, x) == True and sample[y - 1][x] == 0:
                        cost += 1
                        result.append(cost)
                        sample[y - 1][x] = 1
                        BFS(y - 1, x, cost)
                    elif up(y - 1, x) == True and sample[y - 1][x] == 1:
                        cost -= 1
                        result.append(cost)
                        BFS(y - 1, x, cost)
                    else:
                        if left(y, x - 1) == True and sample[y][x - 1] == 0:
                            cost += 1
                            result.append(cost)
                            sample[y][x - 1] = 1
                            BFS(y, x - 1, cost)
                        elif up(y, x - 1) == True and sample[y - 1][x] == 1:
                            cost -= 1
                            result.append(cost)
                            BFS(y, x - 1, cost)
                        else:
                            return -1
    BFS(0, 0, 1)
    return result[-1]

did = solution(maps)
print(did)

