brown = 24
yellow = 24

def solution(brown, yellow):
    answer = []
    lis = []
    for i in range(1, brown + yellow + 1):
        if (brown + yellow) % i == 0:
            lis.append(i)

    for i in lis:
        for k in lis:
            if i * k == brown + yellow:
                if (i-2)*(k-2) == yellow:
                    answer.append(i)
                    answer.append(k)
                    answer.sort()
                    answer.reverse()
                    return answer

did = solution(brown, yellow)
print(did)