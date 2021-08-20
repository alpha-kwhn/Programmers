prices = [1, 2, 3, 2, 3, 1]


def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        if i != len(prices) - 1:
            for k in range(i+1, len(prices)):
                if prices[k] >= prices[i]:
                    count += 1
                if prices[k] < prices[i]: #가격이 prices[i]보다 낮은것이 나오면 카운트를 세어주고 즉시 break
                    count += 1
                    break
            answer.append(count)
        else:
            answer.append(0)
    return answer

did = solution(prices)
print(did)
