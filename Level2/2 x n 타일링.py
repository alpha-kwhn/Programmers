def solution(n):
    lis = [0, 1, 2, 3]
    if n <= 3:
        return n
    else:
        for i in range(4, n+1):
            lis.append((lis[i-1] + lis[i-2]) % 1000000007)
        return lis[n]