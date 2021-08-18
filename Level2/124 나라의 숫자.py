n = 11

def solution(n):
    answer = ''
    while n > 0:
        answer += '124'[(n-1) % 3]
        n = (n-1) // 3
    answer = answer[::-1]
    return answer

did = solution(n)
print(did)







did = solution(n)
print(did)


