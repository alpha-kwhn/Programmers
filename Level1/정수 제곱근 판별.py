n = 121


def solution(n):
    answer = 0
    tmp = n ** 0.5
    if (tmp - int(tmp)) == 0.0:
        answer = (tmp+1) * (tmp+1)
        answer = int(answer)
    else:
        answer = -1
    return answer

did = solution(n)
print(did)