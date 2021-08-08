x = 2
n = 5


def solution(x, n):
    answer = []
    term = x
    for i in range(n):
        answer.append(x)
        x += term
    return answer

did = solution(x, n)
print(did)