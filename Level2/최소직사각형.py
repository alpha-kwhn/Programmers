sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]

def solution(sizes):
    garo = []
    sero = []
    for i in range(0, len(sizes)):
        garo.append(max(sizes[i][0], sizes[i][1]))
        sero.append(min(sizes[i][0], sizes[i][1]))
    return max(garo) * max(sero)

did = solution(sizes)
print(did)