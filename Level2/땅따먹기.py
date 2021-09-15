land = [[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]

def solution(land):
    total = []
    def BFS(index, count, result):
        if count < len(land) - 1:
            tmp = []
            for i in range(4):
                if i != index:
                    tmp.append(i)
            BFS(tmp[0], count + 1, result + land[count][tmp[0]])
            BFS(tmp[1], count + 1, result + land[count][tmp[1]])
            BFS(tmp[2], count + 1, result + land[count][tmp[2]])
        else:
            tmp = []
            for i in range(4):
                if i != index:
                    tmp.append(i)
            total.append(result + land[count][tmp[0]])
            total.append(result + land[count][tmp[1]])
            total.append(result + land[count][tmp[2]])
    BFS(0, 0, 0)
    BFS(1, 0, 0)
    BFS(2, 0, 0)
    BFS(3, 0, 0)
    return max(total)


did = solution(land)
print(did)