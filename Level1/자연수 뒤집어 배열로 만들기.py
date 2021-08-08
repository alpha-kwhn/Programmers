n = 12345


def solution(n):
    tmp = str(n)
    lis = []

    for i in range(len(tmp)):
        lis.append(tmp[i])
    lis = list(map(int, lis))
    lis.reverse()
    return lis

did = solution(n)
print(did)