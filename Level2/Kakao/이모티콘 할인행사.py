# 가입자 최대한 늘리기
# 판매액 최대한 늘리기
# 할인률은 10, 20, 30, 40% 중 하나
# n명의 카톡 사용자들에게 m개의 이모티콘 할인판매
# 자신의 기준에 따라 일정 비율 이상 할인 하는 이모티콘 모두 구매
# 구매한 이모티콘 비용 합이 일정 가격 이상 -> 구매 모두 취소하고 플러스 서비스 가입
from itertools import product


def solution(users, emoticons):
    eventPrice = [0.9, 0.8, 0.7, 0.6]
    discountMin = list(list(zip(*users))[0])
    maxPurchase = list(list(zip(*users))[1])
    result = []

    # 이모티콘 할인 경우의 수 모음
    cases = list(product(eventPrice, repeat=len(emoticons)))
    finalPrice = []

    # 이모티콘 할인 경우의 수 별 최종 판매될 금액 구하기
    for item in cases:
        finalPrice.append([x * y for x, y in zip(item, emoticons)])

    for case in range(len(cases)):
        subscribe = 0
        money = 0
        for user in range(len(users)):
            total = 0
            able = False
            for idx in range(len(emoticons)):
                if 1 - (discountMin[user] * 0.01) < cases[case][idx]:
                    continue
                else:
                    total += finalPrice[case][idx]
                    if total >= maxPurchase[user]:
                        subscribe += 1
                        able = False
                        break
                    else:
                        able = True
            if able is True:
                money += total

        result.append([subscribe, money])

    result = sorted(result, key=lambda x: (-x[0], -x[1]))
    return result[0]