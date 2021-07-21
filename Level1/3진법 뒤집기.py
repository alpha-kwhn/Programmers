n = 125
n1 = 125


def solution(n):
    tmp = ''

    while n > 0:
        n, mod = divmod(n, 3) #10진법을 3진법으로
        tmp += str(mod)

    answer = int(tmp, 3) #3진법을 10진법으로
    return answer


did = solution(n)
print(did)