from itertools import permutations
numbers = "011"

def solution(numbers):
    lis = []
    answer = []
    pro = []
    tmp = []
    solve = []
    for i in range(len(numbers)):
        lis.append(numbers[i])

    for k in range(1, len(numbers) + 1):
        npr = list(map(''.join, permutations(lis, k)))
        answer.append(npr)

    for v in answer:
        for j in range(len(v)):
            if v[j] not in pro:
                pro.append(v[j])

    for p in pro:
        if p[0] != '0':
            tmp.append(p)
    tmp = list(map(int, tmp))

    for t in tmp:
        if t != 1:
            flag = 1
            for i in range(2, t):
                if t % i == 0:
                    flag = 0
                    break
            if flag == 1:
                solve.append(t)
    return len(solve)



did = solution(numbers)
print(did)