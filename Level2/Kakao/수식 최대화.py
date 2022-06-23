expression = "100-200*300-500+20"

from itertools import permutations


def operates(k, a, b):
    if k == '+':
        return a + b
    elif k == '-':
        return a - b
    else:
        return a * b


def solution(expression):
    operations = ['*', '+', '-']
    lis = []
    result = ''

    # 숫자와 연산자 분리해서 리스트에 저장해 줌
    for i in range(len(expression)):
        if expression[i] not in operations:
            result += expression[i]
            if i == len(expression) - 1:
                lis.append(int(result))
        else:
            lis.append(int(result))
            lis.append(expression[i])
            result = ''

    # 연산자 우선순위 조합 경우의 수 구하기
    combi = permutations('+*-', 3)
    answer = []

    for i in combi:
        tmp = lis
        for j in range(3):
            updates = []
            for p in range(len(tmp)):
                if p == 0:
                    updates.append(tmp[0])
                else:
                    if tmp[p - 1] != i[j]:
                        updates.append(tmp[p])
                    else:
                        newer = operates(updates[-1], updates[-2], tmp[p])
                        updates.pop()
                        updates.pop()
                        updates.append(newer)
            tmp = updates
        answer.append(abs(updates[0]))
    return max(answer)




did = solution(expression)
print(did)