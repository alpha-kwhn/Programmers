n = 11

def solution(n):
    tmp = str(n)
    lis = []
    for i in range(len(tmp)):
        lis.append(tmp[i])
    lis = list(map(int, lis))
    ss = sum(lis)
    if n % ss == 0:
        return True
    else:
        return False

did = solution(n)
print(did)