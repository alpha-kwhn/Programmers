n = 3

def solution(n):

    if n % 2 == 0:
        answer = "수박"*(n // 2)
        return answer

    else:
        answer = "수박"*(n//2) + "수"
        return answer

did = solution(n)
print(did)