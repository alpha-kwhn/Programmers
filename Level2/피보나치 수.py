n = 5

def solution(n):
    lis = [0, 1]
    for i in range(n-1):
        tmp = lis[i] + lis[i+1]
        lis.append(tmp)
    return lis[n] % 1234567


did = solution(n)
print(did)