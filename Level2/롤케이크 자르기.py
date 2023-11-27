from collections import Counter

def solution(topping):
    answer = 0
    cake = Counter(topping)
    friend = set()

    for idx in range(len(topping)):
        cake[topping[idx]] -= 1
        friend.add(topping[idx])

        if cake[topping[idx]] == 0:
            cake.pop(topping[idx])

        if len(cake) == len(friend):
            answer += 1
    return answer






