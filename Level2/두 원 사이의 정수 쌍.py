import math

def solution(r1, r2):
    answer = 0

    for x in range(1, r2+1, 1):
        a = math.sqrt(r2 ** 2 - x ** 2)
        a = int(a)
        a = a*2+1
        b = 0

        if x < r1:
            b = math.sqrt(r1*r1 - x*x)
            if b == (int)(b):
                b = b*2-1
            else:
                b = (int)(b)
                b = b*2+1

        answer += (a-b)

    answer = answer * 2
    answer = answer + 2 * (r2 - r1 + 1)

    return answer