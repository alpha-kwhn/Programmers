# 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기 구매
# 제한수치보다 큰 공격력 무기 사야하면, 정해진 공격력 가진 무기 구매
# 공격력 1 == 철 1키로

def yaksu(num):
    count = 0
    for i in range(1, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            count += 1
            if i ** 2 != num:
                count += 1
    return count


def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        if yaksu(i) > limit:
            answer += power
        else:
            answer += yaksu(i)

    return answer