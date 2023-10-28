def solution(dots):
    answer = 0
    dots = sorted(dots, key=lambda x: (x[0], x[1]))
    answer = abs(dots[0][1] - dots[1][1]) * abs(dots[0][0] - dots[2][0])
    return answer
