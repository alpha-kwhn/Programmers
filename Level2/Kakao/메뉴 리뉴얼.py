from itertools import combinations

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]


def solution(orders, course):

    for i in range(len(orders)):
        tmp = list(orders[i])
        tmp.sort()
        orders[i] = ''.join(tmp)

    answer = []
    for i in orders:
        lis = []
        for j in range(len(i)):
            lis.append(i[j])
        for p in range(len(course)):
            ncr = list(map(''.join, combinations(lis, course[p])))
            if len(ncr) != 0:
                answer.append(ncr)
    lit = []
    for i in answer:
        lit += i
    lit.sort(key = len)

    for i in lit:
        if lit.count(i) < 2:
            lit.remove(i)

    for i in lit:
        if lit.count(i) < 2:
            lit.remove(i)

    big = [0] * len(course)
    te = 0
    pear = 0
    for i in range(len(lit) - 1):
        if len(lit[i+1]) != course[te]:
            big[te] = lit[pear:i+1]
            te += 1
            pear = i + 1
    big[te] = lit[pear:]

    if 0 in big:
        big.remove(0)
    if 0 in big:
        big.remove(0)

    for i in range(len(big)):
        remain = []
        maxi = big[i].count(big[i][0])
        remain.append(big[i][0])
        for j in range(1, len(big[i])):
            if big[i].count(big[i][j]) > maxi:
                maxi = big[i].count(big[i][j])
                while len(remain) != 0:
                    remain.pop()
                remain.append(big[i][j])
            elif big[i].count(big[i][j]) == maxi:
                maxi = big[i].count(big[i][j])
                remain.append(big[i][j])
        big[i] = remain

    for i in range(len(big)):
        big[i] = list(set(big[i]))

    final = []
    for i in range(len(big)):
        final += big[i]
    final.sort()

    return final



did = solution(orders, course)
print(did)