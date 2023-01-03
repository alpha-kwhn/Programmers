def solution(t, p):
    tmp = len(p)
    answer = 0

    for i in range(0, len(t)):
        if int(t[i:i + tmp]) <= int(p) and (i + tmp) <= len(t):
            answer += 1
    return answer