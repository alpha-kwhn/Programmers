def solution(k, d):
    answer = 0

    for i in range((d // k) + 1):
        target = int(((d ** 2) - ((i * k) ** 2)) ** (1 / 2))
        answer += ((target // k) + 1)

    return answer
