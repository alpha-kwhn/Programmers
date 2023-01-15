# 빵 (1) - 야채(2) - 고기(3) - 빵(1)
# 높이무시

def solution(ingredient):
    answer = []
    count = 0

    for i in ingredient:
        if len(answer) >= 4:
            if answer[-4:] == [1, 2, 3, 1]:
                del answer[-4:]
                count += 1

        answer.append(i)

        if answer[-4:] == [1, 2, 3, 1]:
            del answer[-4:]
            count += 1

    return count