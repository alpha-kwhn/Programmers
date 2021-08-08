price = 3
money = 20
count = 4
result = 10

def solution(price, money, count):
    answer = 0
    num = 1
    for i in range(count):
        answer += (num * price)
        num += 1
    if money - answer >= 0:
        return 0
    else:
        answer = abs(money - answer)
        return answer

did = solution(price, money, count)
print(did)