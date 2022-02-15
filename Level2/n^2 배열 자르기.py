n = 4
left = 7
right = 14

def solution(n, left, right):
    answer = []
    for i in range(int(left), int(right)+1):
        if i % n > i // n:
            answer.append((i % n) + 1)
        elif i % n == i // n:
            answer.append((i // n) + 1)
        elif i % n < i // n:
            answer.append((i // n) + 1)
    return answer

print(solution(n, left, right))


