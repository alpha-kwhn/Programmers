from itertools import combinations

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]


def solution(orders, course):

    for i in range(len(orders)):
        tmp = list(orders[i])
        tmp.sort()
        orders[i] = ''.join(tmp)
    #문자열 오름차순 정렬 시행

    answer = []
    for i in orders:
        lis = []
        for j in range(len(i)):
            lis.append(i[j])
        for p in range(len(course)):
            ncr = list(map(''.join, combinations(lis, course[p])))
            if len(ncr) != 0:
                answer.append(ncr)
    #모든 주문의 조합 생성

    lit = []
    for i in answer:
        lit += i
    lit.sort(key = len)
    #리스트 합쳐서 단일화

    for i in lit[:]:
        if lit.count(i) < 2:
            lit.remove(i)
    #갯수가 2개 미만인 요소들은 전부 지우기 (복사본을 이용)

    big = [0] * len(course)
    te = 0
    pear = 0
    for i in range(len(lit) - 1):
        if len(lit[i+1]) != course[te]:
            big[te] = lit[pear:i+1]
            te += 1
            pear = i + 1
    big[te] = lit[pear:]
    #코스요리 길이별로 나눠서 리스트에 저장

    for i in big[:]:
        if i == 0:
            big.remove(0)
    #리스트에 0이 존재한다면 0을 다 삭제해야함

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
    #각 길이별 코스요리 중에서 주문횟수가 가장 많았던 것들만 남기고 나머지는 다 삭제

    for i in range(len(big)):
        big[i] = list(set(big[i]))
    #중복 요소 제거

    final = []
    for i in range(len(big)):
        final += big[i]
    final.sort()
    #리스트를 전부 합친 후 오름차순 정렬

    return final



did = solution(orders, course)
print(did)