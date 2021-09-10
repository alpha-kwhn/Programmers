N = 8
A = 1
B = 2

def solution(n, a, b):
    small = min(a, b)
    big = max(a, b)

    if small % 2 == 1:
        small += 1
    if big % 2 == 1:
        big += 1
    if small == big:
        return 1

    count = 0
    while small != big:
        if small != 1:
            if small % 2 == 1:
                small += 1
            if big % 2 == 1:
                big += 1
            small //= 2
            big //= 2
        elif small == 1:
            if big % 2 == 1:
                big += 1
            big //= 2
        count += 1
    return count




did = solution(N, A, B)
print(did)

