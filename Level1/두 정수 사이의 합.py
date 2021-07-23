a = 5
b = 3

def solution(a, b):
    m = max(a, b)
    n = min(a, b)
    first = (n*(n+1)) // 2
    second = (m*(m+1)) // 2
    answer = (second - first) + n
    return answer

did = solution(a, b)
print(did)