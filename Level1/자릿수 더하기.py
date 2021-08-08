n = 987


def solution(n):
    answer = 0
    lis = []
    tmp = str(n)

    for i in range(len(tmp)):
        lis.append(tmp[i])

    lis = [int(i) for i in lis]

    for i in range(len(lis)):
        answer += lis[i]

    return answer


did = solution(n)
print(did)