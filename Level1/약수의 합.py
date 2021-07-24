n = 12

def solution(n):
    sums = []
    for i in range(1, n+1):
        if n % i == 0:
            sums.append(i)
    answer = sum(sums)
    return answer

did = solution(n)
print(did)