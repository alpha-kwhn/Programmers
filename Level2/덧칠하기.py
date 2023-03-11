def solution(n, m, section):
    answer = 1
    maximum = section[0] + (m - 1)

    if len(section) == 1:
        return 1
    else:
        for i in range(1, len(section)):
            if section[i] <= maximum:
                continue
            else:
                maximum = section[i] + (m - 1)
                answer += 1
        return answer