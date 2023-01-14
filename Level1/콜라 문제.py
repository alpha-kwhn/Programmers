def solution(a, b, n):
    answer = 0

    while True:
        tmp = n // a
        answer += (b * tmp)
        n = n - (tmp * a) + (b * tmp)

        if n < a:
            break

    return answer