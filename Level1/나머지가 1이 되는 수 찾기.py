n = 12

def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i

print(solution(n))

