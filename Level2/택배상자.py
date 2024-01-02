def solution(order):
    bag = []
    start = 0
    answer = 0
    lens = len(order)

    for i in range(lens):
        bag.append(i + 1)

        while bag and bag[-1] == order[start]:
            bag.pop()
            answer += 1
            start += 1

    return answer
